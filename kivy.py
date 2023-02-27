from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import json

szöveg= "Szeretném közölni a játékossal, hogy ez a játék Tomó halálával végződik legtöbb esetben csak erős tűrőképességel bíróknak ajánljuk ezt a tartalmat."

def on_button_click(e):
        print(e)

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalandjáték")
        self.master.configure(background="#261401")


        # változó számú gombok létrehozása
        self.szint_szovegek()
        self.create_buttons()



    def szint_szovegek(self):
       text = Text(root, height=10, width=100,font=("Arial", 25))
       text.pack(pady=10)
       text.insert("end", szöveg)
    



    def create_buttons(self):
        # szint változó meghatározása
        szintek = [10,15,16,17,165,]

   
        # a gombok létrehozása a szint változótól függően
        for i in range(len(szintek)):
            self.button = tk.Button(self.master, text=f"{szintek[i]}",font=("Arial", 30), command=on_button_click(self)) 
            self.button.pack(pady=15)
    
    

   


root = tk.Tk()
myapp = MyApp(root)
root.mainloop()
