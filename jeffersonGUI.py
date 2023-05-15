"""from tkinter import *

window = Tk()
window.geometry("1200x700")
window.title("Cylinder Jefferson")
window.iconbitmap("th.ico")





window.mainloop()
"""

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
root.configure(bg='black')



# Zone de texte pour le texte à chiffrer/déchiffrer
input_text = Text(root, height=10, width=50,  bg='black', fg="red")
input_text.grid(row=6, column=1, padx=10, pady=10)

# Boutons de chiffrement/déchiffrement
encrypt_button = Button(root, text="Chiffrer", command=encrypt, bg='black', fg="red")
encrypt_button.grid(row=6, column=2, padx=10, pady=10)
decrypt_button = Button(root, text="Déchiffrer", command=decrypt, bg='black', fg="red")
decrypt_button.grid(row=7, column=2, padx=10, pady=10)

# Zone de texte pour le résultat
output_text = Text(root, height=10, width=50,  bg='black', fg="red")
output_text.grid(row=6, column=3, columnspan=3, padx=10, pady=10)

root.mainloop()
