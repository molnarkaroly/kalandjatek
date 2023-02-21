import tkinter
import tkinter as tk
import keyboard
import time
from re import A
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from time import *

sor = 0

szöveg = 1

while True:
    if keyboard.is_pressed('a'):
        szöveg += 1
        


def update():

    szöveg_label.config()

 


    root.after(1000,update)

root = tk.Tk()
root.title('Kaland játék')
root.configure(background="#120b0b")

# Teljes képernyős mód beállítása
root.attributes('-fullscreen', True)

# Ablak bezárásának kezelése
def close(event):
    root.attributes('-fullscreen', False)
    root.destroy()

# ESC billentyű lenyomásának kezelése
root.bind('<Escape>', close)


szöveg_label = Label(root, text=szöveg, font=("Diediedie",45),fg="black", bg="green")
szöveg_label.pack()



# Ablak megnyitása
root.mainloop()

