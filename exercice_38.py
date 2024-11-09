# Ecrire une fonction qui supprime les doublons d'une liste 
# On renvoit la liste dans doublons et par ordre croissant

def clean_list(list):

    for element in list:
        element_occurence = list.count(element)

        if element_occurence >= 2:

            for i in range(element_occurence-1):
                list.remove(element)

    list.sort()

    return list

print(clean_list([0,3,5,7,3,5,1,-1]))
print(clean_list([0,5,9,10,3.2,1,-3]))

#  Autre solution

def clean_list_set(lst):

    lst = set(lst)
    lst = list(lst)

    lst.sort()
    return lst     

print(clean_list_set([0,3,5,7,3,5,1,-1]))
print(clean_list_set([0,5,9,10,3.2,1,-3]))     