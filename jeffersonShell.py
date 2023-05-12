
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







# <--------------------------------------- Test------------------------------------------------------------------>
"""
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().replace('\n', '')

def substitution_polyalphabetic_cipher(key, plaintext):
    alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ciphertext = ''
    for letter in plaintext:
        if letter in alphabets:
            alphabet_index = key.index(alphabets.index(letter))
            alphabet = alphabets[alphabet_index]
            ciphertext += alphabet
        else:
            ciphertext += letter
    return ciphertext

filename = 'cylinderWiki.txt'
key = [7,9,5,10,1,6,3,8,2,4]
plaintext = 'Retreat Now'

text = read_file(filename)
ciphertext = substitution_polyalphabetic_cipher(key, plaintext.upper())

print('Plain text:', plaintext)
print('Cipher text:', ciphertext)

"""