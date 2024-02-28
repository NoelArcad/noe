# Fonction pour calculer l'indice de masse corporelle (IMC)
def calculer_imc(poids, taille):
    return poids / (taille ** 2)

# Fonction pour déterminer la catégorie de poids
def determiner_categorie_imc(imc):
    if imc < 18.5:
        return "Maigre"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Surpoids"
    else:
        return "Obèse"

# Demander à l'utilisateur son âge
age = int(input("Entrez votre âge : "))

# Demander à l'utilisateur son poids en kg
poids = float(input("Entrez votre poids en kg : "))

# Demander à l'utilisateur sa taille en mètres
taille = float(input("Entrez votre taille en mètres : "))

# Calculer l'IMC
imc = calculer_imc(poids, taille)

# Déterminer la catégorie de poids
categorie_imc = determiner_categorie_imc(imc)

# Afficher les résultats
print(f"Votre age est de {age}, votre taille {taille} et votre poids {poids}")
print(f"\nVotre IMC est : {imc:.2f}")
print(f"Catégorie de poids : {categorie_imc}")




