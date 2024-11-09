# Ecrire une fonction qui prend un dictionnaire en paramètre et renvoie le nombre de valeur contenu dans les listes associées aux clés

def number_of_value(dict):

    sum_of_values = 0

    for element in dict.values():
        sum_of_values += len(element)

    return sum_of_values


print(number_of_value({
    "a":[1,2,3],
    "b":[3,"p"],
    "c":[8]
}))

print(number_of_value({
    "Julie":[10,30.1],
    "Fred":[26,75.6],
    "David":[]
}))