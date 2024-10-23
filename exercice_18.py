# Trier une liste de tuples dans un ordre croissant en se basant sur le deuxièmme élément

my_list = [("Pomme", 15), ("Banane", 8), ("Fraise", 12), ("Kiwi", 9), ("Pêche", 2)]

my_list = sorted(my_list, key= lambda element: element[1])

print(my_list)

# Solution

my_list.sort(key = lambda x: x[1])