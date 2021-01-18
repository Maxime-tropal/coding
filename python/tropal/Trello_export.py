import os, time, pyperclip
from tkinter import Label, Button, Tk


os.chdir("C:\\Users\\mmi\\Desktop\\DEV\\python\\tropal")
os.startfile("Trello.bat")
time.sleep(5)
with open("lien_telechargement.txt", "r") as f:
    result = []
    for lines in f:
        result = lines.split("\":\"")
        

lien_dl = str([result[-1]])
lien_dl = lien_dl[:-4]
print(lien_dl)


def copylink(fenetre):
    pyperclip.copy("https://trello.com/" + lien_dl)
    pyperclip.paste()
    label1 = Label(text="Lien copié dans le presse papier !")
    label1.pack()

root = Tk()
root.geometry("300x100")



btn1= Button(root,text="Copier le lien de téléchargement", command=lambda: copylink(root))
btn1.pack()

root.mainloop()
    