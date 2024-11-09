# Ecrire un algorithme qui dessine une moitié pyramide d'étoile allant de 1, puis 2 puis 4 puis 6 etc 

for star in range(1, 11):
    
    if star % 2 == 0 or star == 1:
        print("*"*star)
