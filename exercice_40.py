# Ecrire une fonction maximum qui retourne le nombre maximum d'une liste sans utiliser la méthode max

def max(list):

    max_number = list[0]

    for element in list:
        if element > max_number:
            max_number = element
    
    return max_number

print(max([-9,2,4,1,8]))
print(max([-3,1,7,6,2,3]))