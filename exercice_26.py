# Supprimer un élément d'une liste

my_list = [1,2,3,4,5]
index = 0

for i in range(len(my_list)):
     
    if my_list[i] == 1:
        index = i

my_list.pop(index)

print(my_list)

# Solution

my_list.remove(1)