import os, time, requests
from tkinter import Label, Button, Tk


os.chdir("C:\\Users\\mmi\\Documents\\GitHub\\coding\\python\\tropal")
os.startfile("Trello.bat")
time.sleep(5)
with open("lien_trello.txt", "r") as f:
    result = []
    for lines in f:
        result = lines.split("\":\"")
        

lien_dl = str([result[-1]])
lien_dl = lien_dl[2:-6]

lien_dl_final = "https://trello.com" + lien_dl

print(lien_dl_final)

response = requests.get(lien_dl_final, verify=False, auth=("34fc8c60f8adc6a5065b3164efd629e0", "271bce676bf1a7a040f05058d412dae83144c75a2ec23cf428b9bab178d15e69"))
print(response.text)