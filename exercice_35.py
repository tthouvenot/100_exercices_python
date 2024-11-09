# Ecrire une fonction VérifPresence(a, L) prenant en paramètre une liste et un élément A
# La fonction retourne True si A est présent dans la liste et False sinon

def inside_list(a, list):

    for element in list:
        if element == a:
            return True

    return False
        
print(inside_list(2, [1,2,3,4,5,6]))
print(inside_list(-1, [3,6,9,7,"abcr"]))

# Solution
def inside_list_2(a, list):

    if a in list:
        return True
    else:
        return False
    
print(inside_list_2(2, [1,2,3,4,5,6]))
print(inside_list_2(-1, [3,6,9,7,"abcr"]))