import os, glob, time, pathlib, datetime, tkinter.messagebox
from tkcalendar import *
from os import startfile
from tkinter import Tk, Button, Label, Toplevel




def maintest():

    def my_function(input_dir, output_name):
        filesinfo = []  # création d'une liste vide
        today = datetime.datetime.today()  # récupère la date du pc
        os.chdir(input_dir)
        for fichiers in glob.glob("**", recursive=True): # récupère tout les fichiers dans le dossier
            modified_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(fichiers))
            path = os.path.abspath(fichiers)
            duration = today - modified_date
            if duration.seconds > 43200 and duration.days < 5:
                filesinfo.append(f"{modified_date} = {path}")
        writefile(filesinfo, output_name)

    def writefile(filesinfo, output_name):
        with open(output_name, "a+") as f:
            for item in filesinfo:
                f.write(item + "\n\n")

    def incrementfile():
        today = datetime.datetime.today().date()
        path = pathlib.Path("//10.2.30.61/c$/Qlikview_Tropal/Raport")
        inc = len(list(path.glob(f"{today}*")))+1
        outfile = path/f"{today}_{inc}.txt"
        return outfile

    output_name = incrementfile()
    repertoires = ["//10.2.30.61/c$/Qlikview_Tropal/Apps/", "//10.2.30.61/c$/Qlikview_Tropal_Paie/Apps/",
                    "//10.2.30.61/c$/Qlikview_Jastres/apps/", "//10.2.30.61/c$/Qlikview_Compta/SuiviCompta/apps/"]
    for item in repertoires:
        input_dir = item
        my_function(input_dir, output_name)
    os.startfile(str(output_name))
    exit

def opennewwindow(cal2):
    global newWindow
    newWindow = Toplevel(root)
    newWindow.title("Resultats")
    #newWindow.geometry("350")
    init(cal2)

def init(cal3):
    dateSelect = setdate(cal3)
    files = []
    os.chdir("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\")
    for file in glob.glob(dateSelect + "_*.txt"):
        files.append(file)

    nbfile = len(files)
    def buttonWindows(var):
        newWindow.geometry(var)
        rowz = 2
        resultat = 1
        for i in range(nbfile):
            i=i+1
            button = Button(newWindow, text="Resultat " + str(resultat), command=lambda i=i: opentext(i,dateSelect))
            button.grid()
            button.config(height=3, width=20)
            rowz +=3
            resultat +=1
    
    if nbfile <=3:
        buttonWindows("300x175")  
    elif nbfile <=5:
        buttonWindows("300x300")
    elif nbfile <=7:
        buttonWindows("300x400")
    elif nbfile <=9:
        buttonWindows("300x525")
        
    else:
        tkinter.messagebox.showerror("Attention !", "Le nombre de boutons doit être inférieur a 10 !")
        buttonWindows("300x1000")

def opentext(x, nvdate):
    
    x = str(x)
    if os.path.isfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + nvdate + "_" + x + ".txt") == True:
        startfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + nvdate + "_" + x + ".txt")
    else:
        tkinter.messagebox.showerror("Attention !", "Le script n'a pas encore été lancé " + x + " fois aujourd'hui.")

def setdate(cal4):
    datechoisie = cal4.get_date()
    # conversion de la date au bon format 27-11-2020 -> 2020-11-27
    # On split le premier format dans une liste, on inverse l'ordre du 1er et dernier item et on le remet dans la l
    datechoisie = datechoisie.replace("/", "-")
    datechoisie = datechoisie.split('-')
    datechoisie = "-".join(reversed(datechoisie))
    
    return datechoisie 
    
def primary1(windows):
    d = datetime.date.today()
    cal = Calendar(windows, selectmode="day", year=d.year, month=d.month, day=d.day)
    cal.grid(row=2, column= 3, rowspan=5)

    datebutton = Button(windows, text="Validez la date", command=lambda: opennewwindow(cal))
    datebutton.grid(row=8, column=3, rowspan=2)
    datebutton.config(height=4, width=20)
    testbutton = Button(windows, text="TEST", command=maintest, bg="red")
    testbutton.grid(row=16, column=3, rowspan=2)
    testbutton.config(height=4, width=20)    
    

today = str(datetime.datetime.today().date())

root = Tk()
root.geometry("370x550")
root.title("Vérification rechargement des QVW")

primary1(root)

col_count, row_count = root.grid_size()

for col in range(col_count):
    root.grid_columnconfigure(col, minsize=20)

for row in range(row_count):
    root.grid_rowconfigure(row, minsize=20)

root.mainloop()
