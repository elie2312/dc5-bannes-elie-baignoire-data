phrase = input("Saisissez votre phrase : ")

phrase_maj = ""

for lettre in phrase:
    if 'a' <= lettre <= 'z':
        maj = chr(ord(lettre) - 32)
        phrase_maj += maj
    else:
        phrase_maj += lettre

phrase_min = ""

for lettre in phrase:
    if 'A' <= lettre <= 'Z':
        min = chr(ord(lettre) + 32)
        phrase_min += min
    else:
        phrase_min += lettre

nbmots = 0
for i, char in enumerate(phrase):
    if char.isalnum():
        if i + 1 == len(phrase) or not phrase[i + 1].isalnum():
            nbmots += 1
    else:
        if not char.isspace():
            if i + 1 == len(phrase) or phrase[i + 1].isspace() or phrase[i + 1].isalnum():
                nbmots += 1

print(phrase_maj)
print(phrase_min)
print(nbmots)