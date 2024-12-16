# Faire une fonction qui prend un chemin complet vers un fichier et lit son contenu.
import sys

def read_file_content(path):

    file = open(path, 'r')

    content = file.read()

    file.close()

    return content

print(read_file_content(r'C:\Users\kurdtkobane\Desktop\hello_world.txt'))