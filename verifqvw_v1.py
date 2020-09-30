import os, glob, time, datetime

def my_function(output_name, input_dir):
    with open(output_name, "w+") as f:
        os.chdir(input_dir)
        for fichiers in glob.glob("*"):
            today = datetime.datetime.today()
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(fichiers))
            duration = today - modified_date
            if duration.days < 5:
                f.write(f"{fichiers} = {duration} \n")
    f.close()

arguments = { "//10.2.30.61/c$/temp/test1.txt" : "//10.2.30.61/c$/Qlikview_Tropal/Apps/Ventes", 
              "//10.2.30.61/c$/temp/test1.txt" : "//10.2.30.61/c$/Qlikview_Tropal/Apps/Marge",
              "//10.2.30.61/c$/temp/test1.txt" : "//10.2.30.61/c$/Qlikview_Tropal/apps/prod"}
for output_name, input_dir in arguments.items():
    my_function(output_name, input_dir)