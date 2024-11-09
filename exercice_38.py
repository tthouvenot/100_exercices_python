# Ecrire une fonction qui supprime les doublons d'une liste 
# On renvoit la liste dans doublons et par ordre croissant

def clean_list(list):

    for elem in list:

        element = elem

        for i in range(len(list)):

            if element == list[i]:
                