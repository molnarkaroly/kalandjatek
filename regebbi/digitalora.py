from re import A
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from time import *


def update():
    time_string = strftime(" %I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    win.after(1000,update)


win=Tk()
win.title('Digitális Óra')


win.geometry("500x250")
win.resizable(False, False)


label=Label(win)


color=colorchooser.askcolor() 

colorname=color[1]

win.configure(background=colorname)


time_label = Label(win,font=("Diediedie",45),fg="black", bg=colorname)
time_label.pack()


date_label = Label(win,font=("PWScratchy",35, "bold"), bg=colorname)
date_label.pack() 

#Born Addict
day_label = Label(win,font=("PWScratchy",25), bg=colorname)
day_label.pack()

print(colorname)


update()


win.mainloop()
