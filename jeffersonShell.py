import random

n = 10  # nombre d'entiers à permuter
liste_entiers = list(range(1, n+1))  # liste des entiers à permuter
permutation = random.sample(liste_entiers, n)  # génération de la permutation

print(permutation)  # affichage de la permutation générée

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


def est_permutation(L):
    # Vérification de la longueur de la liste
    if len(L) != max(L):
        return False

    # Vérification des éléments de la liste
    for i in range(len(L)):
        if L[i] != i + 1:
            return False

    # Vérification des entiers compris entre 1 et n
    if sorted(set(L)) != list(range(1, len(L) + 1)):
        return False

    return True
