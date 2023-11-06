liste_nombres = [11, 23, 12, 67, 91, 32, 18, 61, 42, 34]

maximum = liste_nombres[0]
minimum = liste_nombres[0]

for nombre in liste_nombres:
    if nombre > maximum:
        maximum = nombre
    if nombre < minimum:
        minimum = nombre

somme = 0
for nombre in liste_nombres:
    somme += nombre

moyenne = somme / len(liste_nombres)

print("Maximum :", maximum)
print("Minimum :", minimum)
print("Moyenne :", moyenne)
