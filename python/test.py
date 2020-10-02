from tkinter import * 

test1 = Tk()

topFrame = Frame(test1)
topFrame.pack()
bottomFrame = Frame(test1)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Click me", fg="red")
button2 = Button(topFrame, text="No click me", fg="blue")
button3 = Button(topFrame, text="Click me !!", fg="green")
button4 = Button(bottomFrame, text="CLICK", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=RIGHT)
button4.pack(side=BOTTOM)


test1.mainloop()