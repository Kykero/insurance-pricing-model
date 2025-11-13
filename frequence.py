import numpy as np
import pandas as pd

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
