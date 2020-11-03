from tkinter import *
import os

def printtest():
    print("works")

def opentext1():
    from os import startfile
    startfile("C:/Users/maxem/Documents/test1.txt")
    
test1 = Tk()
test1.geometry("800x600")

testbutton = Button(test1, text="TEST", command=printtest)
testbutton.grid(row=16, column=30)
testbutton.config(height=4, width=20)

resultat1 = Button(test1, text="Resultat 1", command=opentext1)
resultat1.grid(row=2, column=30)
resultat1.config(height=4, width=20)

resultat2 = Button(test1, text="Resultat 1", command=opentext1)
resultat2.grid(row=6, column=30)
resultat2.config(height=4, width=20)

resultat3 = Button(test1, text="Resultat 1", command=opentext1)
resultat3.grid(row=10, column=30)
resultat3.config(height=4, width=20)


col_count, row_count = test1.grid_size()

for col in range(col_count):
    test1.grid_columnconfigure(col, minsize=20)

for row in range(row_count):
    test1.grid_rowconfigure(row, minsize=20)

test1.mainloop()