import os, glob, time, ctypes, pathlib

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

def verif():
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
    
def lecture():
    with open(cheminref,"r") as f:
        for line in f:
            listecsv = line.split(";")
            # liste.strip() enlève le dernier bout de chaque item de la liste a savoir le \n ici
            listecsv[-1] = listecsv[-1].strip()
            #séparation des 2 colonnes ccourt et nvccourt en 2 listes différentes
            ccourt.append(listecsv[0])
            nvccourt.append(listecsv[2])

    with open(chemintxt + nomtexte ,"r") as f: 
        for line in f:
            liste = line.split(";")
            champs = liste[7]
            #print(liste[7])
        # string.find permet de compter le nb d'occurence. if str.find = -1 signifie 'si tu ne trouves aucune occurence' et !=-1 si tu trouves au moins 1
        # occurence dans la string
        # donc ici: champs.find permet de voir si il trouve une valeur identique à une liste de réf, et si oui la remplace par une valeur.
            for a,b in zip(ccourt,nvccourt):    
                if champs.find(a):
                    liste[7]=b
                    print(a)
                elif champs.find(a) not in str(liste[7]):
                    ctypes.windll.user32.MessageBoxW(0, "Ces fournisseurs ne sont pas dans le fichier de référence: " + liste[7], "Attention", 1)
                    
            ligne = ';'.join(liste)
            listefinale.append(ligne)

def ecriture():
    os.rename(chemintxt + nomtexte, archive + nomtexte )
    with open("\\\\vifprod1\\ascii\\abattage\\elisa\\brive\\pesée.txt","w") as f:
        for element in listefinale:
            f.write(element)

nomtexte = nbtxt(chemintxt)
verif()
lecture()
#ecriture()