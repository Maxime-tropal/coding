import os,glob,time

cheminbl = "\\\\srvbureautique\\tropalcommun\\informatique\\metro\\bl"
cheminretourmetro = "\\\\srvbureautique\\tropalcommun\\informatique\\metro\\retour metro"

listebl = []
today1 = datetime.datetime.today().date()

def nbbltoday(input_dir):
    