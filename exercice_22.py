# Tronquer un nombre décimal à 2 chiffre après la virgule

decimal = 187.632587

new_decimal = round(decimal, 2)

print(new_decimal)

# solution

float("{:.2f}".format(decimal))