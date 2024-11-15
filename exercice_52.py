#  Créer une fonction qui permet de trouver tous les nombres entre 0 et y divisible par n et qui ne sont pas des multiple de a

def find_divider(n, a, y):

    list_divider = []

    for num in range(0 ,y+1, 1):

        if num % n == 0 and num % a != 0:
            list_divider.append(num)

    return list_divider

print(find_divider(5, 2, 100))
print(find_divider(11,3,85))
