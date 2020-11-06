from tkinter import *
from tkcalendar import*

root= Tk()
root.title("test")
root.geometry("800x600")


cal= Calendar(root, selectmode="day", year=2020, month=11, day=5)
cal.pack(pady=20)

def grab_date():
        mylabel.config(text=cal.get_date())

button1 = Button(root, text= "get date", command=grab_date)
button1.pack(pady=20)

mylabel = Label(root, text="")

root.mainloop()