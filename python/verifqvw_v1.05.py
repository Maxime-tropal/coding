import os, glob, time, datetime

def my_function(input_dir,output_name):
    filesinfo = [] #création d'une liste vide
    today = datetime.datetime.today() #récupère la date du pc
    os.chdir(input_dir) 
    for fichiers in glob.glob("**", recursive=True): #récupère tout les fichiers dans le dossier
        modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(fichiers))
        path = os.path.abspath(fichiers)
        duration = today - modified_date
        if duration.days > 1 and duration.days < 5:
            filesinfo.append(f"{modified_date} = {path}")
    writefile(filesinfo,output_name)
            
def writefile(filesinfo,output_name):
    with open(output_name,"a+") as f:
        for item in filesinfo:
            f.write(item + "\n\n")

def incrementfile():
    todayday = datetime.datetime.today().date()
    output_folder = "//10.2.30.61/c$/Qlikview_Tropal/Raport/"
    highest_num = 0
    for f in os.listdir(output_folder):
        if os.path.isfile(os.path.join(output_folder, f)):
            file_name = os.path.splitext(f)[0]
            try:
                file_num = int(file_name)
                if file_num > highest_num:
                    highest_num = file_num
            except ValueError:
                print("The file name %s is not an integer. Skipping" % file_name)

    output_file = os.path.join(output_folder, str(highest_num + 1) + f"{todayday}" + ".txt")
    return output_file
# liste de liste mettre l'appel des fonctions dans une liste
output_name = incrementfile()
repertoires = ["//10.2.30.61/c$/Qlikview_Tropal/Apps/", "//10.2.30.61/c$/Qlikview_Tropal_Paie/Apps/", "//10.2.30.61/c$/Qlikview_Jastres/apps/", "//10.2.30.61/c$/Qlikview_Compta/SuiviCompta/apps/"]
for item in repertoires:
    input_dir = item
    my_function(input_dir,output_name)
exit

