# variables :
# paquet : liste
# k : entier

# les lignes 7 à 9 ajoutent une valeure aléatoire à la variable temp 
# cet algorithme mélange 49 fois le jeu de cartes

import random

paquet = [1,2,3,4,5,6,7,8,9,10]
k = 0

while k <49:
    i = random.randint(0,9)
    j = random.randint(0,9)
    temp = paquet[i]
    paquet[i] = paquet[j]
    paquet[j] = temp
    k +=1

print(paquet)

#Variables :
# paquetA <- [0...5] entiers
# paquetB <- [0...5] entiers
# a : 0 
# b : 1 
# c : 0

# Début
#
#   pour i de paquet:
#       ajouter paquet[0] à paquetA
#       ajouter 2 à k
#       ajouter paquet[1] à 
#


#a = 0
#b = 0
#c = 0

#paquetA = [0,0,0,0,0]
#paquetB = [0,0,0,0,0]

#for item in paquet:
#    if(a%2 == 1):
#        paquetA[b] = item
#        a = a+1
#        print(paquetA)
#    else:
#        paquetB[c] = item
#        c = c+1
#    i +=1

#print(paquetA)
#print(paquetB)

#ne fonctionne pas mais j'ai essayé
# pour faire quand même l'exercice 6 j'utilise :

paquetA = paquet[0::2]
paquetB = paquet[1::2]
print(paquetA)
print(paquetB)

points1 = 0
points2 = 0
i = 0

for x in paquetA:
    if x > paquetB[i]:
        points1 +=1
        print("Pli " + str(i) + ": " + str(x) + " " +  ">" + " " + str(paquetB[i]) + " donc joueur 1 + 1point")
    else:
        points2 +=1
        print("Pli " + str(i) + ": " + str(x) + " " +  ">" + " " + str(paquetA[i]) + " donc joueur 2 + 1point")
    i += 1
print("Score J1 : ", points1)
print("Score J2 : ", points2)
if points1 > points2:
    print("Le joueur 1 a gagné !")
else:
    print('Le joueur 2 a gagné !')