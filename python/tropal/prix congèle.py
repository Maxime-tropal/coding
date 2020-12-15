import os, glob, time, ctypes, pathlib, ctypes
from tkinter import Tk, Button, Label, Toplevel, Entry
from tkcalendar import *
from datetime import datetime, date, timedelta


cheminref = "\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Referentiels\\prix_congele.csv"
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
    change = input1.get()
    if change == "":
        ctypes.windll.user32.MessageBoxW(0, "Vous devez saisir un code article !", "Attention",1)
    else:
        result = 0
        for item in liste_ouverture:
            if change == item[0]:
                result +=1
        if result >0:
            newWindow()

def enregistrement(cal1,prix1):
    liste_date_Fin = []
    input_calendar = cal1.get_date()
    input_prix2 = prix1.get()
    liste_modif = ouverture()
    liste_modif2 =[]
    change = input1.get()
    for item in liste_modif:
        if change == item[0]:
            dateFin = datetime.strptime(item[4], "%d/%m/%Y").date()
            liste_date_Fin.append(dateFin)
    maxDateFin = max(liste_date_Fin)
    maxDateFin = str(maxDateFin)
    maxDateFin = maxDateFin.split("-")
    maxDateFin = "/".join(reversed(maxDateFin))
    for item in liste_modif:
        if change == item[0] and item[4]==maxDateFin:
            item[4]=conversion_date(input_calendar)
            
        liste_modif2.append([item[0], item[1], item[2], item[3], item[4]])

    print(liste_modif2)




# prend date du calendrier, enlève 1 jour et appelle fonction
def jour_avant(input_calendar):
    date1 = datetime.strptime(input_calendar, "%d/%m/%Y").date()
    date2 = date1 - timedelta(days=1)
    conversion_date(input_calendar)


# argument date = type date, conversion en string et retourne au format dd/mm/yyyy
def conversion_date(date):   
    strdate = str(date)
    strdate = strdate.split("-")
    strdate = "/".join(reversed(strdate))
    return strdate

def newWindow():
    new_window = Toplevel(root)
    input_prix = Entry(new_window)
    d = date.today()
    bouton_valide = Button(new_window, text="Validez", command=lambda: enregistrement(cal, input_prix))
    cal = Calendar(new_window, selectmode="day", year=d.year, month=d.month, day=d.day)
    cal.pack()
    input_prix.pack()
    bouton_valide.pack()

root = Tk()
root.geometry("300x250")

button_changer = Button(text= "Changer", command=changement)
input1 = Entry(root)
button_changer.pack()
input1.pack()
root.mainloop()
