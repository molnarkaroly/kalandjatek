import tkinter
import tkinter as tk
import keyboard
import time
from re import A
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

sor = 0




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

lista = ["alma", "alpaka", "albatrosz",]

def hide_button_1():
    button1.pack_forget()
    label.config(text= lista[0])

def hide_button_2():
    button2.pack_forget()
    label.config(text=lista[1])

def hide_button_3():
    button3.pack_forget()
    label.config(text=lista[2])

def hide_button_4():
    button4.pack_forget()
    label.config(text=lista[3])

utak = [1,2,3,4]

szint= 0

if szint == 0:
    utak =[1,2,3,4]
 

if szint == 1:
    utak =[2,3,4]

if szint == 3:
    utak =[1,4]    

if szint == 4:
    utak =[1]

label = tk.Label(root, text="")
label.pack(pady=5)

if len(utak) == 1:
    button1 = tk.Button(root, text= utak[0], command=hide_button_1)
    szint = utak[0]
    button1.pack(pady=10)
    



if len(utak) == 2:
    button1 = tk.Button(root, text=utak[0], command=hide_button_1)
    szint = utak[0]
    button1.pack(pady=10)

    button2 = tk.Button(root, text=utak[1], command=hide_button_2)
    szint = utak[1]
    button2.pack(pady=10)


if len(utak) == 3:
    button1 = tk.Button(root, text=utak[0], command=hide_button_1)
    szint = utak[0]
    button1.pack(pady=10)

    button2 = tk.Button(root, text=utak[1], command=hide_button_2)
    szint = utak[1]
    button2.pack(pady=10)

    button3 = tk.Button(root, text=utak[2], command=hide_button_3)
    szint = utak[2]
    button3.pack(pady=10)

if len(utak) == 3:
    button1 = tk.Button(root, text=utak[0], command=hide_button_1)
    szint = utak[0]
    button1.pack(pady=10)

    button2 = tk.Button(root, text=utak[1], command=hide_button_2)
    szint = utak[1]
    button2.pack(pady=10)

    button3 = tk.Button(root, text=utak[2], command=hide_button_3)
    szint = utak[2]
    button3.pack(pady=10)

    button4 = tk.Button(root, text=utak[2], command=hide_button_4)
    szint = utak[3]
    button4.pack(pady=10)



#button1 = tk.Button(root, text="Click you!", command=hide_button_1)
#button1.pack(pady=10)

#button2 = tk.Button(root, text="Click me!", command=hide_button_2)
#button2.pack(pady=10)

#button3 = tk.Button(root, text="Click me!", command=hide_button_3)
#button3.pack(pady=10)


button4 = tk.Button(root, text=utak[3], command=hide_button_3)
button4.pack(pady=10)

# Ablak megnyitása
root.mainloop()

