liste= []
listecsv = []
listefinale = []
ccourt=[]
nvccourt=[]
with open("C:\\Users\\mmi\\Desktop\\Classeur1.csv","r") as f:
    for line in f:
        listecsv = line.split(";")
        listecsv[-1] = listecsv[-1].strip()
        print(listecsv)
        #séparation des 2 colonnes ccourt et nvccourt en 2 listes différentes
        ccourt.append(listecsv[0])
        nvccourt.append(listecsv[2])

with open("C:\\Users\\mmi\\Desktop\\e_20111031.txt","r") as f: 
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



with open("C:\\Users\\mmi\\Desktop\\pesée.txt","w") as f:
    for element in listefinale:
        f.write(element)
    