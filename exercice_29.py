# Mélanger aléatoirement les éléments d'une liste
import random

my_list = [3,6,8,7,2,"s", "ch", "d"]

print(f"Avant mélange: {my_list}")

for element in my_list:

    element_index = my_list.index(element)
    random_index = None

    random_index = random.randint(0, len(my_list))

    my_list.pop(element_index)
    my_list.insert(random_index, element)



print(my_list)

print(f"Après mélange: {my_list}")


# Solution
print(f"Avant mélange: {my_list}")

random.shuffle(my_list)

print(f"Après mélange: {my_list}")