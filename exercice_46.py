# Ecrire une fonction qui renvoit tous les diviseurs positifs de n dans un ordre croissant

def divider(number):

    list_of_divider = []

    for i in range(number+1):
        
        if i > 0 and number % i == 0:
            print(i, True)
            list_of_divider.append(i)
        else:
            print(i, False)

    return list_of_divider

print(divider(9))
print(divider(3))
print(divider(321))
print(divider(300))