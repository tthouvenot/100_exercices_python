# Ecrire une fonction qui concatène 2 dictionnaire

def concat_dict(dict1, dict2):

    for key, value in dict2.items():

        dict1[key] = value

    return dict1

print(concat_dict({
    "a":3,
    "b":6,
},
{
    "c":2,
    "d":-1,
}))

print(concat_dict({
    "d":[2,9,4.1],
    "b":6,
},
{
    "p":[]
}))

# Autre solution

def better_concat(dict1, dict2):

    dict1.update(dict2)

    return dict1

print(better_concat({
    "a":3,
    "b":6,
},
{
    "c":2,
    "d":-1,
}))

print(better_concat({
    "d":[2,9,4.1],
    "b":6,
},
{
    "p":[]
}))
