import tkinter as tk
import tkinter.messagebox
from tkinter import *


root = Tk()
root.geometry("800x800")
# nombre de bouton maximum 6 
def start(nbButton):

    if nbButton <=6:
        buttons = []
        rowz = 2
        for i in range(nbButton):
            button = Button(root, command=lambda i=i: printtest(i))
            button.grid(row=rowz, column=19)
            button.config(height=4, width=20)
            rowz +=2
    else:
        tkinter.messagebox.showerror("Attention !", "Le nombre de boutons doit être inférieur a 6 !")
        root.destroy()

#msg erreur 

def printtest(i):
        print("test ok")

start(6)

col_count, row_count = root.grid_size()

for col in range(col_count):
    root.grid_columnconfigure(col, minsize=31)

for row in range(row_count):
    root.grid_rowconfigure(row, minsize=31)

root.mainloop()