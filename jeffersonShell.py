import random

lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generer_ligne():
    ligne = ""
    for j in range(26):
        lettre = random.choice(lettres)
        ligne += lettre
    return ligne

def ecrire_fichier(nom_fichier, n):
    with open(nom_fichier, "w") as f:
        for i in range(n):
            ligne = generer_ligne()
            f.write(ligne + "\n")

ecrire_fichier("dictionnaire.txt", 10)


# Ouvrir le fichier en lecture
with open("dictionnaire.txt", "r") as f:
    # Créer une liste contenant chaque ligne du fichier
    lines = f.readlines()

# Créer un dictionnaire avec les lignes du fichier
dictionnaire = {i+1: lines[i].strip() for i in range(len(lines))}

# Afficher les lignes superposées
for i in range(len(dictionnaire[1])):
    for j in range(1, len(dictionnaire)+1):
        print(dictionnaire[j][i], end=' ')
    print()