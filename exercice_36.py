# Faire un code qui calcule la somme des chiffres d'un nombre
# Afficher les résultat

def sum (number):

    if number // 10 == 0:
        return number
    else:
        return number % 10 + sum(number // 10)

print(sum(3048))

# solution

number = 3018

number = str(number)
sum_number = 0

for elem in number:
    sum_number += int(elem)

print(sum_number)