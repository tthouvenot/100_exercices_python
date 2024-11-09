# Ecrire une fonction qui prend 3 listes en paramètre et renvoie une concaténation des 3 listes

def concat_lists(l1, l2, l3):

    for element in l2:
        l1.append(element)

    for element in l3:
        l1.append(element)

    return l1

print(concat_lists([0,9,8],[2,6,9],[True,False,"abc"]))
print(concat_lists([[38,-1],3,-9],["xz","France"],[]))