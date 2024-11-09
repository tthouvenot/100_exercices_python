# Ecrire une fonction f(a,b,x) qui prend 3 entiers en paramètres
# La fonction retourne la fonction suivante:
#       f(abx) = a*(x**3) + 2*a*(x**2) + b

def calcul (a,b,x):
    return a*(x**3) + 2*a*(x**2) + b

print(calcul(3,0,1))
print(calcul(0,2,2))
