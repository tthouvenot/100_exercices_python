# Ecrire une fonction qui prend un phrase en paramètre et renvoie true si elle contient au moins une majuscule

def have_uppercase(string):

    for letter in string:
        
        if letter.isupper():
            return True

    return False


        
print(have_uppercase("Les légumes sont bon pour la santé"))
print(have_uppercase("j'apprends le langage python"))
print(have_uppercase("J'ai plusieurs Majuscule"))
    