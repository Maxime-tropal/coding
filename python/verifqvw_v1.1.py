import os, glob, time, pathlib, datetime, tkinter.messagebox
from tkcalendar import Calendar
from os import startfile
from tkinter import Tk, Button, Toplevel

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
    exit

def init():

    files = []
    os.chdir("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\")
    for file in glob.glob("*.txt"):
        files.append(file)
    
    nbfile = len(files)
    nbfile

    if nbfile <=7:
        rowz = 2
        resultat = 1
        for i in range(nbfile):
            i=i+1
            button = Button(root, text="Resultat " + str(resultat), command=lambda i=i: opentext(i))
            button.grid(row=rowz, column=19)
            button.config(height=4, width=20)
            rowz +=3
            resultat +=1
            
    else:
        tkinter.messagebox.showerror("Attention !", "Le nombre de boutons doit être inférieur a 7 !")
        root.destroy()

def opentext(x):
    
    x = str(x)
    if os.path.isfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + today + "_" + x + ".txt") == True:
        startfile("\\\\10.2.30.61\\c$\\Qlikview_Tropal\\Raport\\" + today + "_" + x + ".txt")
    else:
        tkinter.messagebox.showerror("Attention !", "Le script n'a pas encore été lancé " + x + " fois aujourd'hui.")

today = str(datetime.datetime.today().date())
root = Tk()
root.geometry("800x850")

init()

d = datetime.date.today()
cal = Calendar(root, selectmode="day", year=d.year, month=d.month, day=d.day)
cal.grid(row=2, column= 3, rowspan=5)

testbutton = Button(root, text="TEST", command=maintest, bg="red")
testbutton.grid(row=16, column=3, rowspan=2)
testbutton.config(height=4, width=20)

col_count, row_count = root.grid_size()

for col in range(col_count):
    root.grid_columnconfigure(col, minsize=20)

for row in range(row_count):
    root.grid_rowconfigure(row, minsize=20)

root.mainloop()


