# Importation de toutes les classes et fonctions de la bibliothèque Tkinter
from tkinter import *

# Définition de la clé de chiffrement
key = [4, 2, 1, 5, 3, 7,9,14]

def jefferson_cipher(text):
    """
     Fonction de chiffrement
    """
    # Convertit le texte en majuscules
    text = text.upper()
    ciphered_text = ""
    # Pour chaque caractère dans le texte
    for i in range(len(text)):
        # Si le caractère est une lettre
        if text[i].isalpha():
            # Applique le chiffrement de Jefferson sur la lettre et ajoute le résultat à la chaîne de caractères chiffrés
            ciphered_text += chr(((ord(text[i])-65+key[i%len(key)])%26)+65)
        else:
            # Si le caractère n'est pas une lettre, l'ajoute tel quel à la chaîne de caractères chiffrés
            ciphered_text += text[i]
    # Renvoie la chaîne de caractères chiffrés
    return ciphered_text

def jefferson_decipher(ciphered_text):
    """
    Fonction de déchiffrement (inverse du chiffrement)
    """
    deciphered_text = ""
    # Pour chaque caractère dans la chaîne de caractères chiffrés
    for i in range(len(ciphered_text)):
        # Si le caractère est une lettre
        if ciphered_text[i].isalpha():
            # Applique le déchiffrement de Jefferson sur la lettre et ajoute le résultat à la chaîne de caractères déchiffrés
            deciphered_text += chr(((ord(ciphered_text[i])-65-key[i%len(key)])%26)+65)
        else:
            # Si le caractère n'est pas une lettre, l'ajoute tel quel à la chaîne de caractères déchiffrés
            deciphered_text += ciphered_text[i]
    # Renvoie la chaîne de caractères déchiffrés
    return deciphered_text

def encrypt():
    """
     Fonction de gestion de l'événement du bouton de chiffrement
    """
    # Récupère le texte entré par l'utilisateur dans la zone de texte d'entrée
    text = input_text.get("1.0", END).strip()
    # Applique le chiffrement de Jefferson sur le texte et stocke le résultat dans une variable
    ciphered_text = jefferson_cipher(text)
    # Efface le contenu de la zone de texte de sortie
    output_text.delete("1.0", END)
    # Insère le texte chiffré dans la zone de texte de sortie
    output_text.insert("1.0", ciphered_text)

def decrypt():
    """
    Fonction de gestion de l'événement du bouton de déchiffrement
    """
    ciphered_text = input_text.get("1.0", END).strip()
    deciphered_text = jefferson_decipher(ciphered_text)
    output_text.delete("1.0", END)
    output_text.insert("1.0", deciphered_text)

# Interface graphique
root = Tk()
root.title("Chiffrement de Jefferson")
root.iconbitmap("th.ico")
root.configure(bg='#23272a')

# Libellé pour le titre
title_label = Label(root, text="Chiffrement de Jefferson", fg='#ffffff', bg='#23272a', font=('Helvetica', 20))
title_label.grid(row=0, column=1, columnspan=3, pady=20)

# Zone de texte pour le texte à chiffrer/déchiffrer
input_text = Text(root, height=10, width=50, bg='black', fg='red', font=('Helvetica', 12))
input_text.grid(row=1, column=1, padx=20, pady=10)

# Boutons de chiffrement/déchiffrement
encrypt_button = Button(root, text="Chiffrer", command=encrypt, bg='#7289da', fg='#ffffff', font=('Helvetica', 12))
encrypt_button.grid(row=1, column=2, padx=10, pady=10)
decrypt_button = Button(root, text="Déchiffrer", command=decrypt, bg='#7289da', fg='#ffffff', font=('Helvetica', 12))
decrypt_button.grid(row=1, column=3, padx=10, pady=10)

# Zone de texte pour le résultat
output_text = Text(root, height=10, width=50, bg='black', fg='red', font=('Helvetica', 12))
output_text.grid(row=2, column=1, columnspan=3, padx=20, pady=10)

root.mainloop()
