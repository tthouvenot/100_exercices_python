# Créer une fonction qui ajout un élément à un dictionnaire. Elle prend 3 paramètres un dictionnaire, une clé, une valeur.
# La fonction doit ajouter la clé et sa valeur au dictionnaire et renvoyer le dictionnaire modifié.

def add_element_dict(key, value, dictionnary):

    dictionnary[key] = value

    return dictionnary

my_dict = add_element_dict("Baptiste", 20, {
    'julien': 14,
    'Laurent': 31
})
my_dict_2 = add_element_dict("Poids", 63, {})


for key, value in my_dict.items():
    print(f"{key}: {value}")
for key, value in my_dict_2.items():
    print(f"{key}: {value}")