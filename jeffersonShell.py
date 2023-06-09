
import random

n = 10  # nombre d'entiers à permuter
liste_entiers = list(range(1, n+1))  # liste des entiers à permuter
permutation = random.sample(liste_entiers, n)  # génération de la permutation

print(permutation)  # affichage de la permutation générée

lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generer_ligne():
    """
    Ajouter commentaires

    """
    ligne = ""
    for j in range(26):
        lettre = random.choice(lettres)
        ligne += lettre
    return ligne

def ecrire_fichier(nom_fichier, n):
    """
    Ajouter commentaires

    """
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
    """
    Ajouter commentaires

    """
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
    """
    Ajouter commentaires

    """
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

def chiffrement(texte, cylindre, cle):
    """
    Chiffrement d'un texte selon l'algorithme de Jefferson.

        texte (str): Le texte à chiffrer.
        cylindre (dict): Le cylindre sous forme de dictionnaire.
        cle (list of int): La clé, c'est-à-dire l'ordre des cylindres.


    """
    # On commence par supprimer les espaces et mettre le texte en majuscules
    texte = texte.replace(" ", "").upper()

    # On détermine le nombre de cylindres
    nb_cylindres = len(cle)

    # On découpe le texte en blocs de longueur égale au nombre de cylindres
    blocs = [texte[i:i + nb_cylindres] for i in range(0, len(texte), nb_cylindres)]

    # On chiffre chaque bloc
    chiffres = []
    for bloc in blocs:
        chiffre = ""
        for i, lettre in enumerate(bloc):
            # On récupère le cylindre correspondant à la clé
            cylindre_idx = cle[i] - 1
            cyl = cylindre[cylindre_idx + 1]

            # On détermine la position de la lettre dans le cylindre
            pos_lettre = cyl.index(lettre)

            # On chiffre la lettre en prenant la lettre 6 positions après elle dans le cylindre
            chiffre += cyl[(pos_lettre + 6) % 26]

        chiffres.append(chiffre)

    # On retourne les blocs chiffrés concaténés en une seule chaîne de caractères
    return "".join(chiffres)


def dechiffrement(texte, cylindre, cle):
    """
    Déchiffrement d'un texte selon l'algorithme de Jefferson.

        texte : Le texte à déchiffrer.
        cylindre (dict): Le cylindre sous forme de dictionnaire.
        cle (list of int): La clé, c'est-à-dire l'ordre des cylindres.
    """
    # On détermine le nombre de cylindres
    nb_cylindres = len(cle)

    # On découpe le texte en blocs de longueur égale au nombre de cylindres
    blocs = [texte[i:i + nb_cylindres] for i in range(0, len(texte), nb_cylindres)]

    # On déchiffre chaque bloc
    clairs = []
    for bloc in blocs:
        clair = ""
        for i, lettre in enumerate(bloc):
            # On récupère le cylindre correspondant à la clé
            cylindre_idx = cle[i] - 1
            cyl = cylindre[cylindre_idx + 1]

            # On détermine la position de la lettre chiffrée dans le cylindre
            pos_chiffre = cyl.index(lettre)

            # On déchiffre la lettre en prenant la lettre 6 positions avant elle dans le cylindre
            clair += cyl[(pos_chiffre - 6) % 26]

        clairs.append(clair)



#<---------------------------Test n1--------------------------------->
# Ouvrir le fichier contenant le cylindre
with open('1ARIT-MP.txt') as f:
    # Lire les lignes du fichier et les stocker dans une liste
    lines = f.readlines()

# Créer un dictionnaire pour stocker les correspondances de lettres selon le cylindre
cylinder = {}
for i in range(len(lines)):
    # Les lettres sont stockées dans la deuxième colonne de chaque ligne
    cylinder[lines[i][0]] = lines[i][2:].rstrip()

# Convertir la clé fournie en une liste d'indices à utiliser pour accéder au cylindre
key = [i-1 for i in [12, 16, 29, 6, 33, 9, 22, 15, 20, 3, 1, 30, 32, 36, 19, 10, 35, 27, 25, 26, 2, 18, 31, 14, 34, 17, 23, 7, 8, 21, 4, 13, 11, 24, 28, 5]]

# Déchiffrer le texte en utilisant le cylindre et la clé
text = 'GRMYSGBOAAMQGDPEYVWLDFDQQQZXXVMSZFS'
decoded_text = ''
for i in range(len(text)):
    # Trouver la lettre correspondante selon la clé et le cylindre
    letter = cylinder[text[key[i]][0]][int(text[key[i]][1:])-1]
    decoded_text += letter

# Afficher le texte déchiffré
print(decoded_text)





# <--------------------------------------- Test n2------------------------------------------------------------------>
