# Ecrire une fonction qui prend en paramètre: la liste, un index de début et un index de fin.
# On doit retourner la somme de tous les éléments entre le début et la fin

def sum_of_list_element(list, start_index, end_index):

    sum = 0

    for i in range(len(list)):

        if i >= start_index and i <= end_index:
            sum += list[i]
    
    return sum

print(sum_of_list_element([4,10,12,16,18],2,4))
print(sum_of_list_element([2,4,6,8,10,12],0,2))

# Solution:

def somme_list(L, i, j):

    Lij = L[i:j+1]

    somme = 0

    for elt in Lij:

        somme += elt

    return somme

print(somme_list([4,10,12,16,18],2,4))
print(somme_list([2,4,6,8,10,12],0,2))
