# 🧮 Actuarial Pricing with Scikit-learn  
### Modélisation de la prime pure d’un portefeuille d’assurance automobile  

---

## 📘 Contexte

Dans le cadre d’un apprentissage en actuariat et data science, ce projet a pour objectif de **modéliser la prime pure d’assurance auto** à l’aide de modèles statistiques implémentés avec **scikit-learn**.  

En actuariat, la **prime pure** correspond à la valeur attendue du coût des sinistres :  

> 💡 **Prime pure = Fréquence des sinistres × Gravité moyenne des sinistres**

Ce projet vise donc à reproduire la démarche classique des actuaires en combinant deux modèles :
- un **modèle de Poisson** pour la **fréquence** (nombre de sinistres par assuré),
- un **modèle Gamma** pour la **gravité** (montant moyen par sinistre).  

L’ensemble constitue une chaîne de calcul prédictive permettant d’estimer le coût attendu d’un portefeuille d’assurance selon les caractéristiques des assurés et des véhicules.

---
## 🎯 Objectifs du projet

1. **Créer et préparer** un jeu de données représentatif d’un portefeuille d’assurance auto.  
2. **Modéliser la fréquence** des sinistres à l’aide d’une régression de Poisson.  
3. **Modéliser la gravité** des sinistres à l’aide d’une régression Gamma.  
4. **Combiner les deux modèles** pour estimer la prime pure.  
5. **Analyser et visualiser** les résultats pour interprétation actuarielle.  

---


