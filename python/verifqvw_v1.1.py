import os, glob, time, pathlib, datetime, tkinter.messagebox
from tkcalendar import Calendar
from tkinter import *
from os import startfile


def starttest():

    def mainfonction(input_dir, output_name):
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
            lines = f.readlines()
            lines.sort(key = lambda l : l.split('=')[0])
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
        mainfonction(input_dir, output_name)
    exit

today = str(datetime.datetime.today().date())

def opentext1():
    if os.path.isfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + today + "_1.txt") == True:
        startfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + today + "_1.txt")
    else:
        tkinter.messagebox.showerror("Attention !", "Le script n'a pas encore été lancé")

def opentext2():
    if os.path.isfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + today + "_2.txt") == True:
        startfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + today + "_2.txt")
    else:
        tkinter.messagebox.showerror("Attention !", "Le script n'a pas encore été lancé 2 fois")

def opentext3():
    if os.path.isfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + today + "_3.txt") == True:
        startfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + today + "_3.txt")
    else:
        tkinter.messagebox.showerror("Attention !", "Le script n'a pas encore été lancé 3 fois")

root = Tk()
root.geometry("800x700")

d = datetime.date.today()
cal = Calendar(root, selectmode="day", year=d.year, month=d.month, day=d.day)
cal.grid(row=2, column= 3)

testbutton = Button(root, text="TEST", command=starttest)
testbutton.grid(row=16, column=19)
testbutton.config(height=4, width=20)

resultat1 = Button(root, text="Resultat 1", command=opentext1)
resultat1.grid(row=2, column=19)
resultat1.config(height=4, width=20)

resultat2 = Button(root, text="Resultat 2", command=opentext2)
resultat2.grid(row=4, column=19)
resultat2.config(height=4, width=20)

resultat3 = Button(root, text="Resultat 3", command=opentext3)
resultat3.grid(row=8, column=19)
resultat3.config(height=4, width=20)


col_count, row_count = root.grid_size()

for col in range(col_count):
    root.grid_columnconfigure(col, minsize=20)

for row in range(row_count):
    root.grid_rowconfigure(row, minsize=20)

root.mainloop()