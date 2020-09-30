import os, glob, time, datetime

def my_function(input_dir):
    todayday = datetime.datetime.today().date()
    output_name = f"//10.2.30.61/c$/Qlikview_Tropal/raport/{todayday}.txt"
    today = datetime.datetime.today()
    with open(output_name,"a+") as f:
        os.chdir(input_dir)
        for fichiers in glob.glob("**", recursive=True):
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(fichiers))
            path = os.path.abspath(fichiers)
            duration = today - modified_date
            if duration.days > 1 and duration.days < 7:
                f.write(f"{path} = {modified_date} \n\n")
    f.close()

my_function("//10.2.30.61/c$/Qlikview_Tropal/Apps/")
my_function("//10.2.30.61/c$/Qlikview_Tropal_Paie/Apps/")
my_function("//10.2.30.61/c$/Qlikview_Jastres/apps/")
my_function("//10.2.30.61/c$/Qlikview_Compta/SuiviCompta/apps/")
exit

