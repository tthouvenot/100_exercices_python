# On doit calculer le temps d'execution d'un script
# En partant du fichier 24

import time

start_chrono = time.time()

for i in range(0,11):

    print(f"8 x {i} = {8*i}")

end_chrono = time.time()

print(f"Temp écoulé: {end_chrono - start_chrono}")

