# Affciher dans la console les valeurs des clés Pomme, banane du dictionnaire

my_dictionnary = {
    "Pomme": 3,
    "Banane": 7,
    "Kiwi": 1
}

for element in my_dictionnary:

    if element == "Pomme" or element == "Banane":
        print(my_dictionnary[element])

# Solution:
print(my_dictionnary["Pomme"])
print(my_dictionnary["Banane"])