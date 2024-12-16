# Faire une fonction qui compte le nombre d'occurence d'un mot dans un fichier

import os

def word_occurence(path, word):

    file = open(path, 'r')

    content = file.read()

    content_array = content.split(" ")

    count = 0

    for element in content_array:

        element = element.lower().strip(",.?!:;")

        if element == word:
            count += 1

    print(f"Il y a {count} fois le mot {word}")

    file.close()

word_occurence(r"C:\Users\kurdtkobane\Desktop\ma_vieille.txt", 'vieille')