# On crée une fonction qui prend en paramètre 3 listes d'entiers
# On renvoit une liste dans l'ordre croissant qui unifie les 3 listes sans duplication des nombres

def unified_list(list1, list2, list3):

    for i in range(len(list1)-1, -1, -1):
        
        if list1.count(list1[i]) != 1:
            list1.pop(i)

    for element in list3:

        if list1.count(element) == 0:
            list1.append(element)

    for element in list2:
        if list1.count(element) == 0:
            list1.append(element)
        
    list1.sort()

    return list1

print(unified_list([3,6,9,3],[1,0,3],[12,6,0]))
print(unified_list([7,44,-3],[],[7,2,7]))

# Solution

def union_list(l1, l2, l3):

    ens1 = set(l1)
    ens2 = set(l2)
    ens3 = set(l3)

    union_ensemble = ens1 | ens2 | ens3

    list_union = list(union_ensemble)
    list_union.sort()

    return list_union