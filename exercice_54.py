# On crée un fonction qui supprime les espaces d'une phrase et la renvoit

def no_white_space(phrase):

    phrase = phrase.split(' ')
    phrase = ''.join(phrase)

    return phrase

print(no_white_space("La France est belle!"))
print(no_white_space("Je vais prendre mon vélo."))