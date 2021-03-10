#---------- def isTrue()-----------
liste = [7,5,6,"a" == 7]

def isTrue():
    if all(liste) == True:
        return True
    else: 
        return False

test = isTrue()
print(test)

#---------- def dateHeure-----------

from datetime import datetime

def dateHeure():
    ajd = datetime.now()
    ajd = ajd.strftime("%d/%m/%Y %H:%M:%S")
    print("Aujourd'hui = " + str(ajd))

dateHeure()

#---------- classe Email-----------

class Email():
    def __init__(self, body, objet, expediteur, destinataire):
        self.body = body
        self.objet = objet
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.faitle = datetime.now()
        self.misajourle = datetime.now()
        self.envoyele = None

mail1 = Email("corps", "aide python", "moi", "toi")
print(mail1.body + " + " + mail1.objet + " + " + mail1.expediteur + " + " + mail1.destinataire + " + " + str(mail1.faitle) , "+ " + str(mail1.misajourle))


#----------Jeu tour par tour-----------

class Perso():
    def __init__(self, vie, attaque):
        self.vie = vie
        self.attaque = attaque

class Ennemi():
    def __init__(self, vie, attaque):
        self.vie = vie
        self.attaque = attaque

class Main():
    super(Perso, Ennemi)
    def attaque(player,monstre):
        Ennemi.vie - Perso.attaque
        Perso.vie - Ennemi.attaque
        print("Vous : " + Perso.vie + "\n Ennemi : " + Ennemi.vie)

player = Perso(100,15)
monstre = Ennemi(120, 10)

Main.attaque(player, monstre)

'''Créer une classe "Perso" et une classe "Ennemi" en Tour par Tour.
Ensuite créer une classe "Main" qui aura comme méthodes :

		Attaque,
		WhoWin,
		GameOver
'''