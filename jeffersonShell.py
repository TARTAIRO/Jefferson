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

def chiffrement_lettre(lettre, permutation):
    """Chiffre une lettre relativement à une permutation donnée."""
    position = permutation.index(lettre)
    nouvelle_position = (position + 6) % 26
    return permutation[nouvelle_position]

def chiffrement_lettre(permutation, lettre):
    index_lettre = permutation.find(lettre)
    index_chiffre = (index_lettre + 6) % 26
    return permutation[index_chiffre]

# Exemple d'utilisation :
permutation = 'NOZUTWDCVRJLXKISEFAPMYGHBQ'
lettre1 = 'Z'
lettre_chiffree1 = chiffrement_lettre(permutation, lettre1)
print(f"Lettre chiffrée de {lettre1} : {lettre_chiffree1}")

lettre2 = 'B'
lettre_chiffree2 = chiffrement_lettre(permutation, lettre2)
print(f"Lettre chiffrée de {lettre2} : {lettre_chiffree2}")