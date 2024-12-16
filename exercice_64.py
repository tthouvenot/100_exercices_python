#  Faire une fonction qui vérifie si un nombre est présent dans le fichier

import os

def has_number(path, num):

    with open(path, 'r') as file:
        content = file.read()

    if f"{num}" in f"{content}":
        return True
    else:
        return False

print(has_number(r'./has_number.txt', 25))
print(has_number(r'./has_no_number.txt', 25))