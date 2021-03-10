import random


#------------------MENU PRINCIPAL-------------------
def main_menu():
    print("Menu principal\n")
    choix = input("Que voulez vous faire \n\n1) Choisir une table\n2) Calculs aléatoires\n3) Quittez : ")
    if choix == "1":
            choix_table()
    if choix == "2":
        calcul_aléatoire()
    if choix == "quit":
        exit()

#------------------CHOIX DE LA TABLE-------------------
def choix_table():
    liste = range(1,11) # Créer les valeurs de 1 à 10
    table = int(input("Choissiez une table entre " + str(liste[0]) + " et " + str(liste[-1]) + " : "))

    nb = 1
    reponse = lambda chiffre, count: chiffre * count
    while nb <= 10:
        try:
            rep = int(input("\nQuel est le résultat de %d x %d ? " %(table, nb)))
            if rep == reponse(table, nb):
                nb +=1

        except:
            print("\nMauvaise réponse !")
            rep = int(input("\nQuel est le résultat de %d x %d ? " %(table, nb)))

    choix = input("\nBravo ! - Recommencer ? Y/N ")
    if choix.lower() == "y":
        main_menu()
            

#------------------CALCULS ALÉATOIRES-------------------

def calcul_aléatoire():

    x = random.randint(1,10)
    y = random.randint(1,10)
    reponse = input(f"{x} * {y} = ")
    while int(reponse) != (x * y):
        print("Mauvaise réponse, recommence !")
        reponse = input(f"{x} * {y} = ")
        if reponse == "quit":
            exit()
    rematch = input("Bonne réponse, recommencer ? ")
    if rematch == "1":
        calcul_aléatoire()
    if rematch == "2":
        main_menu()


main_menu()
