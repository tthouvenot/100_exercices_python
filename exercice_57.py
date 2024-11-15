# On crée une fonction qui inverse la phrase en paramètre

def reversed_phrase(phrase):

    phrase = phrase.split(" ")
    new_phrase = []

    for word in phrase[::-1]:
        new_phrase.append(word)

    new_phrase = ' '.join(new_phrase)

    return new_phrase

print(reversed_phrase('Hello World!'))
print(reversed_phrase('bonjour tout le monde'))
print(reversed_phrase('Pomme'))

# Solution

def phrase_inverse(phrase):

    phrase = phrase.split(" ")
    phrase = phrase.reverse()
    phrase = ' '.join(phrase)

    return phrase

print(reversed_phrase('Hello World!'))
print(reversed_phrase('bonjour tout le monde'))
print(reversed_phrase('Pomme'))