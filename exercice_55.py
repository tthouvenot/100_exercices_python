# Créer une fonction qui prend en paramètre une liste d'éléments et un élément, on renvoie l'indexe ou les indexes où se trouve l'élément dans la liste
# On retourne une liste d'indexe
# Si pas dans la liste alors on renvoit: "L'élément x n'est pas dans la liste L"

def element_position(list, element):

    result = []

    for i in range(len(list) - 1):

        if element == list[i]:
            result.append(i)

    if len(result) == 0:
        return f"L'élément {element} n'est pas dans la liste {list}"

    return result

print(element_position([1,2,3,6,8,7,3], 3))
print(element_position([6,8,9,1,3,7], -1))