# On crée une méthode qui trouve toutes les voyelles d'une phrase
# Si elle contient une voyelle alors elle renvoit True
# Sinon elle renvoit False

def has_vowels(phrase):

    list_of_vowels = ('a','e','i','o','u','y')

    for letter in (phrase):

        for vowel in list_of_vowels:
            if letter == vowel:
                return True
            
    return False

print(has_vowels('bonjour monde'))
print(has_vowels('je vais prendre ma douche'))
print(has_vowels('bnjr mnd'))

# Solution

def presence_voyelle(phrase):

    voyelles = ['a','e','i','o','u','y']

    for voy in voyelles:

        if voy in phrase:
            return True
        
    return False