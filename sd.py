import tkinter
import tkinter as tk
import keyboard
import time
from re import A
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

sor = 0






def update():

    szöveg_label.config()
    szöveg_label.text()

    root.after(1000,update)

root = tk.Tk()
root.title('Kaland játék')
root.configure(background="#3d2102")

# Teljes képernyős mód beállítása
root.attributes('-fullscreen', True)

# Ablak bezárásának kezelése
def close(event):
    root.attributes('-fullscreen', False)
    root.destroy()

# ESC billentyű lenyomásának kezelése
root.bind('<Escape>', close)

szöveg = 5

szöveg_label = Label(root, text=szöveg, font=("Diediedie",45),fg="#3d2102", bg="green")
szöveg_label.pack()
    

a_button = tk.Button(root, text="ZGrés ", )
a_button.pack()



# Ablak megnyitása
root.mainloop()

