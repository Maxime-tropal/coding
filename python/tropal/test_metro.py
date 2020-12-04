import os, glob, time, pathlib, datetime

cheminbl = "\\\\srvbureautique\\tropalcommun\\informatique\\metro\\bl"
cheminretourmetro = "\\\\srvbureautique\\tropalcommun\\informatique\\metro\\retour metro"

def nbbltoday(cheminbl):
    listebl = []  # création d'une liste vide
    today = datetime.datetime.today()  # récupère la date du pc
    os.chdir(cheminbl)
    for fichiers in glob.glob("**", recursive=True): # récupère tout les fichiers dans le dossier
        modified_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(fichiers))
        path = os.path.abspath(fichiers)
        duration = today - modified_date
        if duration.seconds > 43200 and duration.days < 5:
            filesinfo.append(f"{modified_date} = {path}")
    #writefile(filesinfo, output_name)
            print(filesinfo)

nbbltoday(cheminbl)