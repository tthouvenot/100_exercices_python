# Déclarer une liste L avec la valeur 1,2,3,4,5,6,7,8,9,10
# Puis créer une nouvelle liste L1 qui récupère un élément sur 3
# Enfin afficher la liste L1

my_list = [1,2,3,4,5,6,7,8,9,10]

my_list_2 = []

for i in range(len(my_list)):

    if i % 3 == 0:
        my_list_2.append(my_list[i])

print(my_list_2)