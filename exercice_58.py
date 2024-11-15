# On crée une fonction qui prend en paramètre une liste
# On renvoit une liste de tuple où chaque tuple indique l'élément et le nombre de fois où on le rencontre

def occurence(lst):
    num_of_occurence = 0
    list_of_element = []

    for element in lst:
        found = False
        for i in range(len(list_of_element)):
            if list_of_element[i][0] == element:
                found = True
                break

        if not found:
            num_of_occurence = lst.count(element)
            list_of_element.append((element, num_of_occurence))

    return list_of_element


print(occurence([-4,8,-3,2,1,2,7,9,-3,8,1]))
print(occurence(["a", 3,4,"b","a", 3]))