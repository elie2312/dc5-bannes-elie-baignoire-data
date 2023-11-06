def calcul_factoriel(nombre):
    if nombre < 0:
        return "Le factoriel n'est défini que pour des nombres entiers positifs."
    elif nombre == 0:
        return 1
    else:
        resultat = 1
        for i in range(1, nombre + 1):
            resultat *= i
        return resultat

nombre = 5
factoriel = calcul_factoriel(nombre)
print(f"Le factoriel de {nombre} est {factoriel}")
