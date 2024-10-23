# Faire la somme des valeurs d'un dictionnaire

my_dictionary = {
    "Pomme": 15,
    "Banane": 8,
    "Fraise": 12,
    "Kiwi": 9,
    "Pêche": 2,
}

value_sum = 0

for element in my_dictionary:
    value_sum += my_dictionary[element]

print(value_sum)

# Solution

value_sum = sum(my_dictionary.values())