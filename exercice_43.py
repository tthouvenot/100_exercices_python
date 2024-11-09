# Ecrire une fonction qui prend en paramètre une liste et renvoie la plus petite valeur

def minimum(list):

    minimum_value = list[0]

    for element in list:

        if element < minimum_value:
            minimum_value = element
    
    return minimum_value

print(minimum([-9,2,4,1,8]))
print(minimum([-3,1,7,6,2,3]))