phrase_utilisateur = input("Veuillez saisir une phrase : ")


phrase_majuscules = ""
for char in phrase_utilisateur:
    if 'a' <= char <= 'z':
        phrase_majuscules += chr(ord(char) - 32)
    else:
        phrase_majuscules += char

print("En majuscules :", phrase_majuscules)


phrase_minuscules = ""
for char in phrase_utilisateur:
    if 'A' <= char <= 'Z':
        phrase_minuscules += chr(ord(char) + 32)
    else:
        phrase_minuscules += char

print("En minuscules :", phrase_minuscules)


nombre_mots = 1
for char in phrase_utilisateur:
    if char == ' ':
        nombre_mots += 1

print("Le nombre de mots dans la phrase est de", nombre_mots)