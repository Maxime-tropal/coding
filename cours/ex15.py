moyennes = [14,15,10,9,6,7,19]
somme = 0
nb_moyennes = 0
for i in moyennes:
    somme+=i
nb_moyennes = len(moyennes)
print(somme/nb_moyennes)

moyennes.sort()
print("la meilleure note est", moyennes[-1])

if 10 in moyennes:
    print("la note 10 est présente")
else:
    print("la note 10 n'est pas présente")