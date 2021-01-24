def calcul_moyennes(moyennes):
    somme = 0
    nb_moyennes = 0
    for i in moyennes:
        somme+=i
    nb_moyennes = len(moyennes)
    print(somme/nb_moyennes)

calcul_moyennes([14,15,10,18,6,7,19])