# Ecrire une fonction qui calcule la somme des entiers d'une liste
# On renvoit et affiche la somme

def sum_of_list(list):
    result = 0
    for elem in list:
        result += elem

    return result

print(sum_of_list([3,2,6,9,-1.5]))
print(sum_of_list([-3,-6,0,1,2,7]))