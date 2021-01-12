from random import randint

# crée la liste des coups possibles
t = ["Pierre", "Papier", "Ciseaux"]

# donne un coup aléatoire au computer
computer = t[randint(0,2)]

#initialisation des scores
score_joueur = 0
score_computer = 0
parties = 0

while parties <= 4:
    player = input("Pierre, Papier, Ciseaux? ")
    if player == computer:
        print("Égalité !")
    elif player == "Pierre":
        if computer == "Papier":
            print("Perdu !", computer, "covers", player)
            score_computer +=1
            parties +=1
        else:
            print("Gagné !", player, "smashes", computer)
            score_joueur +=1
            parties +=1
    elif player == "Papier":
        if computer == "Ciseaux":
            print("Perdu !", computer, "cut", player)
            score_computer +=1
            parties +=1
        else:
            print("Gagné !", player, "covers", computer)
            score_joueur +=1
            parties +=1
    elif player == "Ciseaux":
        if computer == "Pierre":
            print("Perdu !", computer, "smashes", player)
            score_computer +=1
            parties +=1
        else:
            print("Gagné !", player, "cut", computer)
            score_joueur +=1
            parties +=1
    else:
        print("Mouvement invalide !")
    print(score_computer , " vs " , score_joueur)

    computer = t[randint(0,2)] # on redonne un coup à l'ordinateur tant que score n'est pas égale a 3

if score_computer < score_joueur:
    print("Vous avez gagné avec", score_joueur , "points !")

else:
    print("L'ordinateur a gagné avec", score_computer , "points !")