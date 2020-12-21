import os, glob, time, ctypes, pathlib, ctypes
from tkinter import Tk, Label, Button, Toplevel, Entry

liste= []
listecsv = []
listefinale = []
ccourt=[]
nvccourt=[]
cheminref = "\\\\vifprod1\\ascii\\abattage\\elisa\\brive\\reference.csv"
chemintxt = "\\\\vifprod1\\ascii\\abattage\\elisa\\brive\\"
archive = "\\\\vifprod1\\ascii\\abattage\\elisa\\brive\\archive\\"

def nbtxt(input_dir):
    os.chdir(input_dir)
    #scan du répertoire \\brive en ne prenant que les fichiers commençant par e_xxxxxx.
    for ftextes in glob.glob("e_*"):
        nomtexte = ftextes
        return nomtexte

def lecture():
    with open(cheminref,"r") as f:
        for line in f:
            listecsv = line.split(";")
            # liste.strip() enlève le dernier bout de chaque item de la liste a savoir le \n ici
            listecsv[-1] = listecsv[-1].strip()
            #séparation des 2 colonnes ccourt et nvccourt en 2 listes différentes
            ccourt.append(listecsv[0])
            nvccourt.append(listecsv[2])

def verif_fichiers():
    csv = pathlib.Path("\\\\vifprod1\\ascii\\abattage\\elisa\\brive\\reference.csv")
    txt = pathlib.Path("\\\\vifprod1\\ascii\\abattage\\elisa\\brive\\" + str(nomtexte))
    if csv.exists():
        pass
    else:
        ctypes.windll.user32.MessageBoxW(0, "Le fichier de référence n'existe pas !", "Attention", 1)
        exit()
    if txt.exists():
        pass
    else:
        ctypes.windll.user32.MessageBoxW(0, "Le fichier texte n'est pas dans le répertoire", "Attention", 1)
        exit()
    
def verif_fournisseurs():
    champs = []
    with open(chemintxt + nomtexte, "r") as f:
        for line in f:
            liste = line.split(";")
            champs.append(liste[7])
    while True:
        try:
            for i in champs:
                no_err_count =0
                for y in ccourt:
                    if i == y:
                        no_err_count +=1
                        
                if no_err_count == 0: 
                    raise ValueError
            break
        except ValueError:
            demande_fournisseur(root)
            break

def demande_fournisseur(fenetre):
    fenetre.title("Fournisseur Inconnu")
    label1 = Label(text="Un des fournisseurs n'existe pas ! Veuillez vérifier et/ou le créer ?")
    bouton_oui = Button(text="Oui", command=creation_fournisseur)
    bouton_non = Button(text="Non", command=Kill)
    label1.pack()
    bouton_oui.pack()
    bouton_non.pack()
    

def creation_fournisseur():
    window_creation = Toplevel(root)
    window_creation.title("Création du code fournisseur")
    window_creation.geometry("300x150")
    label_ccourt = Label(window_creation, text="Saisissez le code court: ")
    label_nvccourt = Label(window_creation, text="Saisissez le nouveau code court: ")
    btn_validation = Button(window_creation, text="Validez les codes", command=lambda: ajout_fournisseur_excel(input_code, input_nvcode))
    input_code = Entry(window_creation)
    input_nvcode = Entry(window_creation)
    label_ccourt.pack()
    input_code.pack()
    label_nvccourt.pack()
    input_nvcode.pack()
    btn_validation.pack()

def ajout_fournisseur_excel(ccourt1, nvccourt1):
    input_ccourt = ccourt1.get()
    input_nvccourt = nvccourt1.get()
    with open(cheminref, "a") as f:
        f.write(input_ccourt + ";" + "" + ";" + input_nvccourt)
        ctypes.windll.user32.MessageBoxW(0, f"Le fournisseur {input_nvccourt} a été ajouté", "Bravo !")
        exit()
        
def Kill():
    exit()

def listing():
    with open(chemintxt + nomtexte ,"r") as f: 
        for line in f:
            liste = line.split(";")
            champs = liste[7]
            for a,b in zip(ccourt,nvccourt):    
                if champs == a:
                    liste[7]= b
                #elif champs.find(a) not in str(liste[7]):
                    #ctypes.windll.user32.MessageBoxW(0, "Ces fournisseurs ne sont pas dans le fichier de référence: " + liste[7], "Attention", 1)   
            ligne = ';'.join(liste)
            listefinale.append(ligne)

def ecriture():
    os.rename(chemintxt + nomtexte, archive + nomtexte)
    with open("\\\\vifprod1\\ascii\\abattage\\elisa\\brive\\pesee.txt","w") as f:
        for element in listefinale:
            f.write(element)
        ctypes.windll.user32.MessageBoxW(0, "L'intégration s'est bien passée !", "Bravo !")
    
root = Tk()
nomtexte = nbtxt(chemintxt)
lecture()
verif_fichiers()
verif_fournisseurs()
listing()
ecriture()
root.mainloop()