# On crée une fonction qui prend en paramètre une phrase et une longueur minimum.
# On filtre la phrase en supprimant tous les mots de longueur strictement inférieur à celle en paramètre
# On retourne la phrase sans le(s) mot(s)

def word_filter(phrase, word_length):

    old_phrase = phrase.split(" ")
    new_phrase = []

    for word in old_phrase:

        if len(word) >= word_length:
            new_phrase.append(word)

    print(new_phrase)

    new_phrase = ' '.join(new_phrase)

    return new_phrase

print(word_filter('Je suis super heureux', 5))
print(word_filter('Salut toi', 4))
print(word_filter('Quel est ton origine?', 5))