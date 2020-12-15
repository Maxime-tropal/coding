import os, glob, time, ctypes, pathlib, ctypes
from tkinter import Tk, Button, Label, Toplevel, Entry
from tkcalendar import *
from datetime import datetime, date, timedelta


cheminref = "\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Referentiels\\prix_congele.csv"
cheminarchive = "\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Referentiels\\archive_prix_congele.csv"
liste_modif_finale =[]

# prend date du calendrier, enlève 1 jour et appelle fonction
def jour_avant(input_calendar):
    date1 = datetime.strptime(input_calendar, "%d/%m/%Y").date()
    date2 = date1 - timedelta(days=1)
    date_string = str(date2)
    date_string = conversion_date(date_string)
    return date_string

# argument date = type string, conversion en string et retourne au format dd/mm/yyyy
def conversion_date(date):   
    
    date = date.split("-")
    date = "/".join(reversed(date))
    return date




def ouverture():
    liste_principale = []
    liste_principale_modif = []
    with open(cheminref,"r") as f:
        for line in f:
            liste_principale = line.split(";")
            liste_principale[-1] = liste_principale[-1].strip()
            liste_principale_modif.append(liste_principale)
        return(liste_principale_modif)

def changement():
    liste_ouverture = ouverture()
    cart = input1.get()
    if cart == "":
        ctypes.windll.user32.MessageBoxW(0, "Vous devez saisir un code article !", "Attention",1)
    else:
        result = 0
        for item in liste_ouverture:
            if cart == item[0]:
                result +=1
        if result >0:
            newWindow()
        else:
            newWindow()
        # bouton oui non , si oui newwindows, si non revenir saisie 
def newWindow():
    new_window = Toplevel(root)
    input_prix = Entry(new_window)
    d = date.today()
    bouton_valide = Button(new_window, text="Validez", command=lambda: validation(cal, input_prix))
    cal = Calendar(new_window, selectmode="day", year=d.year, month=d.month, day=d.day)
    cal.pack()
    input_prix.pack()
    bouton_valide.pack()




def enregistrement_prix_old(cal1,cart):
    liste_date_Fin = []
    liste_modif = ouverture()
    for item in liste_modif:
        if cart == item[0]:
            dateFin = datetime.strptime(item[4], "%d/%m/%Y").date()
            liste_date_Fin.append(dateFin)
    maxDateFin = max(liste_date_Fin)
    maxDateFin = str(maxDateFin)
    maxDateFin = conversion_date(maxDateFin)
    for item in liste_modif:
        if cart == item[0] and item[4]==maxDateFin:
            item[4]=jour_avant(conversion_date(cal1))
            
        liste_modif_finale.append([item[0], item[1], item[2], item[3], item[4]])

def valide_argument(argument,ckoi):
    if argument == "":
        ctypes.windll.user32.MessageBoxW(0, f"Vous devez saisir un {ckoi} !", "Attention",1)
    if ckoi=="prix":
        print(type(argument))
        argument = float(argument)
        return("ok")
        #si erreur faire remonter sur ecran

def ecriture():
    os.rename(cheminref, cheminarchive )
    with open(cheminref,"w") as f:
        for element in liste_modif_finale:
            for item in element:
                print(item)
                #f.write(item)

def validation(cal1,prix1):
    # validation des arguments
    input_prix = prix1.get()
    input_cart = input1.get()
    input_calendar = cal1.get_date()

    if valide_argument(input_prix,"prix") == "ok":
        # modifier la dernière date de fin 
        enregistrement_prix_old(input_calendar,input_cart)
        liste_modif_finale.append([input_cart, "",input_prix , input_calendar, "31/12/2999" ])
        ecriture()
        print('ok')

    # vérification de la cohérence de la demande (si la date que l'on veut modifier est antérieur à une date déjà saisie sur code article) 
    
    
    # ajout de la date et du prix souhaité 
    #print(liste_modif_finale)

root = Tk()
root.geometry("300x250")

button_changer = Button(text= "Changer", command=changement)
input1 = Entry(root)
button_changer.pack()
input1.pack()
root.mainloop()