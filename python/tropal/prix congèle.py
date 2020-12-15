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
    liste_date = []
    input_calendar = cal1.get_date()
    input_prix2 = prix1.get()
    liste_modif = ouverture()
    change = input1.get()
    for item in liste_modif:
        liste_date.append(item[4])
    print(liste_date)
        #liste_date_modif = liste_date[2::2]
    for a,b in zip(liste_modif, liste_date):
        if change == a[0] and b:
            date1 = datetime.strptime(input_calendar, "%d/%m/%Y").date()
            date2 = date1 - timedelta(days=1)
            strdate = str(date2)
            #print(item[4])
            #item[4]= strdate
            strdate = strdate.split("-")
            strdate = "-".join(reversed(strdate))
            #print(item[3])
            

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
