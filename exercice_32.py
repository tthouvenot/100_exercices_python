# Créer une liste avec les valeur 3,6,9,12,15,18,21,24
# Créer une liste en compréhension qui contient les nombres de la liste divisé par 3

my_list = [3,6,9,12,15,18,21,24]

my_list_2 = [x / 3 for x in my_list]

print(my_list_2)