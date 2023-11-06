phrase_utilisateur = input("Entrez une phrase : ")

phrase_majuscules = ""
phrase_minuscules = ""
mots = 0
dans_un_mot = False

for caractere in phrase_utilisateur:
    if caractere.isalpha():
        if dans_un_mot:
            phrase_minuscules += caractere
            phrase_majuscules += caractere.upper()
        else:
            mots += 1
            phrase_minuscules += caractere
            phrase_majuscules += caractere.upper()
            dans_un_mot = True
    else:
        phrase_minuscules += caractere
        phrase_majuscules += caractere.upper()
        dans_un_mot = False

if phrase_utilisateur[-1].isalpha():
    mots += 1

print("Phrase en majuscules :", phrase_majuscules)
print("Phrase en minuscules :", phrase_minuscules)
print("Nombre de mots dans la phrase :", mots)
