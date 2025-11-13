import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import PoissonRegressor
from sklearn.metrics import mean_poisson_deviance
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# ============================
# 1. Chargement des données + Nettoyage simple
# ============================

df = pd.read_csv("freMTPL2freq.csv")

# Nettoyage simple : retrait des expositions nulles
df = df[df["Exposure"] > 0].copy()

# Variable cible
y = df["ClaimNb"]

# Offset = log(exposition)
offset = np.log(df["Exposure"])

# ============================
# 2. Définition des features
# ============================

features_categorique = ["VehBrand", "VehPower", "VehAge", "Region", "Area"]
features_numeric = ["DrivAge", "BonusMalus", "Density"]

preprocessing = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), features_categorique),
        ("num", StandardScaler(), features_numeric),
    ]
)

# ============================
# 3. Pipeline + Modèle Poisson
# ============================

model = Pipeline(
    steps=[
        ("preprocessing", preprocessing),
        ("poisson", PoissonRegressor(alpha=1e-4, max_iter=1000)),
    ]
)

# ============================
# 4. Entraînement
# ============================

print("Entraînement du modèle Poisson…")
model.fit(
    df[features_categorique + features_numeric],
    y,
    poisson__sample_weight=df["Exposure"],
)

# ============================
# 5. Prédictions
# ============================

pred = model.predict(df[features_categorique + features_numeric])

# ============================
# 6. Évaluation
# ============================

deviance = mean_poisson_deviance(y, pred, sample_weight=df["Exposure"])
print(f"\n🔎 Deviance de Poisson : {deviance:.4f}")

# ============================
# 7. Sauvegarde du modèle
# ============================

import joblib

joblib.dump(model, "modele_poisson_frequence.pkl")

print("\nModèle sauvegardé 'modele_poisson_frequence.pkl'")
