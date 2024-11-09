# Ecrire une fonction qui prend une liste en paramètre et renvoie le nombre d'élément sans utiliser la fonction len()

def list_length(list):

    leng = 0

    for element in list:

        leng += 1

    return leng

print(list_length([3,6,7,"abde",[1,3,57], True]))
print(list_length([]))