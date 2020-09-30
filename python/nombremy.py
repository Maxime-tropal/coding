import random

def pasdelettres():
        while True:
            try:
                nombre = int(input("Devinez le nombre mystere : "))
                return nombre
                break
            except:
                print("Pas de lettres !")
def random1():
    nombre_mystere = random.randrange(0, 100)
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




    