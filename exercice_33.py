# Créer une liste avec les valeurs -6,5,-3,-1,2,8,-3.6
# Puis créer une liste avec compréhension qui ne garde que les chiffres supérieur à 0

my_list = [-6,5,-3,-1,2,8,-3.6]

new_list = [x for x in my_list if x >= 0]

print(new_list)