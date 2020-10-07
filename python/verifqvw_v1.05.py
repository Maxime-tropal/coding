import os, glob, time, pathlib, datetime


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
    path = pathlib.Path("T:/Qlikview_Tropal/Raport")
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
