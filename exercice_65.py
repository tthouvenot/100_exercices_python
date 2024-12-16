#  Faire une fonction qui renvoie le nombre de fichier dans un dossier
import os

def files_number(path):

    files_and_folder = os.listdir(path)

    file_count = sum(1 for item in files_and_folder if os.path.isfile(os.path.join(path, item)))

    print(f"Il y a {file_count} dans le dossier {path} .")

files_number(r'R:\Films')