# Déclarer deux listes L1 et L2
# On retourne une liste L3 contenant les éléments en commun

my_list = [9,8,7,14,3,2,"a","p","bonjour","b"]
my_list_2 = ["b", 1,9.2,6,3,9,"p"]
my_list_3 = []

for element in my_list:

    element_1 = element

    for element in my_list_2:

        if element == element_1:
            my_list_3.append(element)

print(my_list_3)

# Solution
L3 = set(my_list_2).intersection(set(my_list))
L3 = list(L3)

print(L3)