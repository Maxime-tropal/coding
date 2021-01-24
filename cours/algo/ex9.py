nombre_caracteres = 8
nombre_chiffres = 2
nombre_lettres = 10
nombre_speciaux = 1
i = 0

if nombre_caracteres >= 8:
    i+=1
if nombre_chiffres >= 1:
    i+=1
if nombre_lettres >= 1:
    i+=1
if nombre_speciaux >= 1:
    i+=1
if i ==4:
    print("mot de passe correct")
else:
    print("mot de passe incorrect")