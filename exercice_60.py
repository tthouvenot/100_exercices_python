# Faire une fonction qui calcul le plus grand commun diviseur à l'aide de l'algo d'euclide.

def greatest_devider(a, b):

    if a <= 0 and b <= 0:
        return print('Erreur: Veuillez entrer une valeur positive.')
    
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a

    return a

print(greatest_devider(3,5))
print(greatest_devider(5,15))
print(greatest_devider(21,15))

# Solution
def calcul_pgcd(a, b):

    # Vérifie si a et b sont supérieur à 0 et renvoie une erreur si c'est pas le cas
    assert(a>0 and b>0)

    while b != 0:

        a,b = b, a%b
    
    return a

print(calcul_pgcd(3,5))
print(calcul_pgcd(5,15))
print(calcul_pgcd(21,15))