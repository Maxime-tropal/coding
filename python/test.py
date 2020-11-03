from tkinter import *   


class Bouttons():

    def __init__(self, master):
        frame = Frame(master, width=200, height=100)
        frame.grid()

        self.clickButton = Button(frame, text="Click me", command= self.printtest)
        self.clickButton.grid(row=0, column=2)

        self.quitbutton = Button(frame, text="Fermer", command=frame.quit)
        self.quitbutton.grid(row=1, column=0)
    
    col_count, row_count =test1.grid_size()

    for col in range(col_count):
            test1.grid_columnconfigure(col, minsize=20)

    for row in range(row_count):
            test1.grid_rowconfigure(row, minsize=20)
    def printtest(self):
        print("test ok")

test1 = Tk()
b = Bouttons(test1)
test1.mainloop()