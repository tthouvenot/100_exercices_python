# Déclarer une variable var avec comme valeur "Bonjour"
# Puis vérifier si var est un int ou un str
#   - Si c'est un int on affiche Entier
#   - Si c'est un str on affiche Chaîne de caractères

var ="Bonjour"

if type(var) is int:
    print("Entier")
elif type(var) is str:
    print("Chaîne de caractères")