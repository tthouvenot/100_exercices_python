# Récupérer l'extension d'un fichier

import os

# On détermine le chemin du fichier qu'on souhaite vérifier
file_path = r'C:\Users\kurdtkobane\Pictures\wallpaper\947133.jpg'

# Donne le nom du fichier
file_name= os.path.basename(file_path)

# Permet de récupérer le dernier élément du split
extension_name = file_name.split('.')[-1]

print(extension_name)