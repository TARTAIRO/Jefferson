from tkinter import *

# Définition de la clé de chiffrement
key = [4, 2, 1, 5, 3, 7]

# Fonction de chiffrement
def jefferson_cipher(text):
    text = text.upper()
    ciphered_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            ciphered_text += chr(((ord(text[i])-65+key[i%len(key)])%26)+65)
        else:
            ciphered_text += text[i]
    return ciphered_text

# Fonction de déchiffrement (inverse du chiffrement)
def jefferson_decipher(ciphered_text):
    deciphered_text = ""
    for i in range(len(ciphered_text)):
        if ciphered_text[i].isalpha():
            deciphered_text += chr(((ord(ciphered_text[i])-65-key[i%len(key)])%26)+65)
        else:
            deciphered_text += ciphered_text[i]
    return deciphered_text

# Fonction de gestion de l'événement du bouton de chiffrement
def encrypt():
    text = input_text.get("1.0", END).strip()
    ciphered_text = jefferson_cipher(text)
    output_text.delete("1.0", END)
    output_text.insert("1.0", ciphered_text)

# Fonction de gestion de l'événement du bouton de déchiffrement
def decrypt():
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
