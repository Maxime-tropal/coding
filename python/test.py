from tkinter import * 

test1 = Tk()

def LeftClick(event): #event permet de lancer la fonction si la condition du bind a été accomplie.
    test2 = Tk()
    new_window = Label(test2, text="this is a test")
    new_window.grid(row=0)
def RightClick(event):
    test3 = Tk()
    new_window = Label(test3, text="this is a test")
    new_window.grid(row=0)   

name = Label(test1, text="Username : ")
password = Label(test1, text="Password : ")
entry1 = Entry(test1)
entry2 = Entry(test1)

name.grid(row=0, sticky=E)  #N-E-S-W north east south west, grid fonctionne comme un tableau excel
password.grid(row=1, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

checkbox = Checkbutton(test1, text="Keep me logged in ?")
checkbox.grid(columnspan=2) #rassemble 2 cellules en 1 seule

button= Button(test1, text="Click me!")
button.bind("<Button-1>", LeftClick) # <Button-1> = click gauche, <Button-2> click molette, <Button-3> click droit
button.bind("<Button-3>", RightClick)
button.grid(row=4)                       #quand on appelle une fonction avec tkinter ne pas mettre les ()

test1.mainloop()  #permet de laisser la fenêtre ouverte en permanence                                      
