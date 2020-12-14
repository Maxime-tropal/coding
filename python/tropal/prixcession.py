import os, glob, time, ctypes, pathlib
from tkinter import Tk, Button, Label, Toplevel, Entry
from tkcalendar import *
from datetime import datetime, date, timedelta


cheminref = "\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Referentiels\\prix_congele.csv"
def ouverture():
    liste_principale = []
    liste_principale1 = []
    with open(cheminref,"r") as f:
        for line in f:
            liste_principale = line.split(";")
            liste_principale[-1] = liste_principale[-1].strip()
            liste_principale1.append(liste_principale)
        return(liste_principale1)

def changement():
    liste1 = ouverture()
    change = input1.get()
    result = 0
    for item in liste1:
        if change == item[0]:
            result +=1
    if result >0:
        newWindow()

def enregistrement(cal1,prix1):
    inputcalendar = cal1.get_date()
    #print(inputcalendar)
    inputprix2 = prix1.get()
    #print(inputprix2)
    liste_modif = ouverture()
    #print(liste_modif)
    change = input1.get()
    #print(change)
    for item in liste_modif:
        if change == item[0] and item[4] == "31/12/2999":
             
            date1 = datetime.strptime(inputcalendar, "%d/%m/%Y").date()
            date2=date1 - timedelta(days=1)
            item[4]= date2
            
def newWindow():
    new_window = Toplevel(root)
    inputprix = Entry(new_window)
    d = date.today()
    bouton_valide = Button(new_window, text="Validez", command=lambda: enregistrement(cal, inputprix))
    cal = Calendar(new_window, selectmode="day", year=d.year, month=d.month, day=d.day)
    cal.pack()
    inputprix.pack()
    bouton_valide.pack()


        
root = Tk()
root.geometry("300x250")

buttonchanger = Button(text= "Changer", command=changement)
input1 = Entry(root)
buttonchanger.pack()
input1.pack()

root.mainloop()
