# Afficher les nombres impairs de 1 à 20 inclus
# Faut utiliser les deux boucles

for i in range(1,20):

    if i % 2 != 0:
        print(i)

cumul = 1

while cumul <= 20:

        if cumul % 2 != 0:
            print(cumul)
        
        cumul += 1