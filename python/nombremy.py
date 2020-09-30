import random

def pasdelettres():
        while True:
            try:
                nombre = int(input("Devinez le nombre mystere : "))
                return nombre
                break
            except:
                print("Pas de lettres !")
def pasdelettres1():
        while True:
            try:
                difficulte = int(input("Choisissez votre difficulte : 1, 2 ou 3 : "))
                while difficulte > 3:
                    difficulte = int(input("Choisissez votre difficulte : 1, 2 ou 3 : "))
                return difficulte
                break
            except:
                print("Pas de lettres !")
def random1():
    difficulte = pasdelettres1()
    if difficulte == 1:
        nombre_mystere = random.randrange(1, 100)
    if difficulte == 2:
        nombre_mystere = random.randrange(1, 1000)
    if difficulte == 3:
        nombre_mystere = random.randrange(1, 10000)
    print(nombre_mystere)
    nombre = pasdelettres()
    while nombre != nombre_mystere:
        if nombre < nombre_mystere:
            print(f"c'est plus grand que {nombre}.")
            nombre = pasdelettres()
        elif nombre > nombre_mystere:
            print(f"c'est plus petit que {nombre}.")
            nombre = pasdelettres()



random1()
print("Bravo, vous avez trouver le nombre mystere !")
choix = int(input("Voulez vous reessayer ? 1 : oui, 2 : non "))
while choix == 1:
    random1()
    print("Bravo, vous avez trouver le nombre mystere !")
    choix = int(input("Voulez vous reessayer ? 1 : oui, 2 : non "))

#mdp


    