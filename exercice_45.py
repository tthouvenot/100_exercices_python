# Ecrire une fonction qui renvoie la moyenne d'une liste

def average(list):

    sum_of_elements = 0

    for element in list:

        sum_of_elements += element

    return sum_of_elements/len(list)


print(average([1,2,3,4,5,6,7]))
print(average([3,0,-1,5,6,9,17]))

# Autre solution

def moyenne(list):

    somme = sum(list)

    return somme/len(list)


print(moyenne([1,2,3,4,5,6,7]))
print(moyenne([3,0,-1,5,6,9,17]))