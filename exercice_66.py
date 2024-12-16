# Faire une fonction qui permet d'écrire un texte dans un fichier

import os

def write_file(path, text):

    with open(path, 'w') as file:
        file.write(text)

    with open(path, 'r') as file:
        content = file.read()

    return content

print(write_file(r'./test_exercice66.txt', "Voici le texte que j'ajoute: Bonjour, je m'appelle Grégory et j'ai 30 ans"))    