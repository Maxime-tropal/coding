from tkinter import * 
import os, glob, time, pathlib, datetime
test1 = Tk()

def LeftClick(event): #event permet de lancer la fonction si la condition du bind a été accomplie.
    test2 = Tk()
    new_window = Label(test2, text="Done !")
    new_window.grid(row=0)
    output_name = incrementfile()
    repertoires = ["//10.2.30.61/c$/Qlikview_Tropal/Apps/", "//10.2.30.61/c$/Qlikview_Tropal_Paie/Apps/",
               "//10.2.30.61/c$/Qlikview_Jastres/apps/", "//10.2.30.61/c$/Qlikview_Compta/SuiviCompta/apps/"]
    for item in repertoires:
        input_dir = item
        my_function(input_dir, output_name)
    exit
 
def my_function(input_dir, output_name):
    filesinfo = []  # création d'une liste vide
    today = datetime.datetime.today()  # récupère la date du pc
    os.chdir(input_dir)
    for fichiers in glob.glob("**", recursive=True): # récupère tout les fichiers dans le dossier
        modified_date = datetime.datetime.fromtimestamp(
            os.path.getmtime(fichiers))
        path = os.path.abspath(fichiers)
        duration = today - modified_date
        if duration.seconds > 18000 and duration.days < 5:
            filesinfo.append(f"{duration} = {path}")
    writefile(filesinfo, output_name)

def writefile(filesinfo, output_name):
    with open(output_name, "a+") as f:
        for item in filesinfo:
            f.write(item + "\n\n")

def incrementfile():
    today = datetime.datetime.today().date()
    path = pathlib.Path("T:/Qlikview_Tropal/Raport")
    inc = len(list(path.glob(f"{today}*")))+1
    outfile = path/f"{today}_{inc}.txt"
    return outfile

name = Label(test1, text="Username : ")
password = Label(test1, text="Password : ")
entry1 = Entry(test1)
entry2 = Entry(test1)

name.grid(row=0, sticky=E)  #N-E-S-W north east south west, grid fonctionne comme un tableau excel
password.grid(row=1, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

checkbox = Checkbutton(test1, text="Keep me logged in ?")
checkbox.grid(columnspan=2) #rassemble 2 cellules en 1 seule

button= Button(test1, text="Click me!")
button.bind("<Button-1>", LeftClick) # <Button-1> = click gauche, <Button-2> click molette, <Button-3> click droit
button.grid(row=4)                       #quand on appelle une fonction avec tkinter ne pas mettre les ()

test1.mainloop()  #permet de laisser la fenêtre ouverte en permanence                                      
