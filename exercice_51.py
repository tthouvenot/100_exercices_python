#  Ecrire une fonction pour calculer la factorielle du nombre entier n
#  On renvoie le résultat

def factorial(number):

    result = 1

    for i in range(number, -1, -1):
        if i == 0:
            break
        else:
            result *= i

    return result

print(factorial(8))
print(factorial(3))
print(factorial(9))
print(factorial(0))

# Solution

def calcul_factoriel(n):

    if n == 0:
        return 1
    
    res_factoriel = n

    for k in range(n-1, 0, -1):
        res_factoriel *= k

    return res_factoriel

print(calcul_factoriel(3))
print(calcul_factoriel(9))
print(calcul_factoriel(0))