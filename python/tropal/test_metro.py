import os, glob, time, pathlib, datetime

cheminbl = "\\\\srvbureautique\\tropalcommun\\informatique\\metro\\bl"
cheminretourmetro = "\\\\srvbureautique\\tropalcommun\\informatique\\metro\\retour metro"

def nbbltoday(cheminbl):
    listebl = []  # création d'une liste vide
    today = datetime.datetime.today()  # récupère la date du pc
    os.chdir(cheminbl)
    for fichiers in glob.glob("**"): # récupère tout les fichiers dans le dossier
        modified_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(fichiers))
        path = os.path.abspath(fichiers)
        duration = today - modified_date
        if duration.days < 1:
            listebl.append(f"{path}")
    for item in listebl:
        bl = os.path.basename(item)
    with open(bl) as f:
        a = f.readlines()
        print(a)
nbbltoday(cheminbl)
