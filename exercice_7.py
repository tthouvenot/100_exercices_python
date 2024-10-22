# Demander à l'utilisateur son âge
# Vérifier si l'utilisateur a un âge supérieur ou inférieur à 18 ans.
#   - S'il a 18 ans ou plus on affiche "l'utilisateur est majeur"
#   - S'il a moins de 18 ans on affiche "l'utilisateur est mineur"

age = int(input("Quel est votre âge?"))

if age < 18 and age >= 0:
    print("L'utilisateur est mineur")
else:
    print("L'utilisateur est majeur")