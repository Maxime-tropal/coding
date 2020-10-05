import os, glob, time, datetime

def my_function(input_dir):
    filesinfo = [] #création d'une liste vide
    today = datetime.datetime.today() #récupère la date du pc
    os.chdir(input_dir) 
    for fichiers in glob.glob("**", recursive=True): #récupère tout les fichiers dans le dossier
        modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(fichiers))
        path = os.path.abspath(fichiers)
        duration = today - modified_date
        if duration.days > 1 and duration.days < 5:
            filesinfo.append(f"{modified_date} = {path}")
    writefile(filesinfo)
            
def writefile(filesinfo):
    todayday = datetime.datetime.today().date()
    output_name = f"//10.2.30.61/c$/temp/{todayday}.txt"
    with open(output_name,"a+") as f:
        for item in filesinfo:
            f.write(item + "\n\n")
# liste de liste mettre l'appel des fonctions dans une liste
repertoires = ["//10.2.30.61/c$/Qlikview_Tropal/Apps/", "//10.2.30.61/c$/Qlikview_Tropal_Paie/Apps/", "//10.2.30.61/c$/Qlikview_Jastres/apps/", "//10.2.30.61/c$/Qlikview_Compta/SuiviCompta/apps/"]
for item in repertoires:
    input_dir = item
    my_function(input_dir)
exit

