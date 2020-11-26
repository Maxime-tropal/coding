import os, glob, time

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

nomtexte = nbtxt(chemintxt)

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
    # string.find permet de compter le nb d'occurence. if str.find = -1 signifie 'si tu ne trouves aucune occurence' et !=-1 si tu trouves au moins 1
    # occurence dans la string
    # donc ici: champs.find permet de voir si il trouve une valeur identique à une liste de réf, et si oui la remplace par une valeur.

        for a,b in zip(ccourt,nvccourt):    
            if champs.find(a) !=-1:
                liste[7]=b
        ligne = ';'.join(liste)
        listefinale.append(ligne)

os.rename(chemintxt + nomtexte, archive + nomtexte )
with open("\\\\vifprod1\\ascii\\abattage\\elisa\\brive\\pesée_" + nomtexte,"w") as f:
    for element in listefinale:
        f.write(element)
