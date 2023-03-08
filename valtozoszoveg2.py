import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import json

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self['command'] = self.on_button_click

    def on_button_click(self):
        szoveg.configure(state='normal')
        szoveg.delete(1.0, END)
        szöveg= {self['text']}
        szoveg.insert("end", f'{szöveg}')
        
        #szoveg.configure(state='disabled')

szintek = [15, 65, 48]
class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalandjáték")
        self.master.configure(background="#261401")
        self.szintek = szintek

        self.szint_szovegek()
        self.create_buttons()

    def szint_szovegek(self):
       global szoveg
       szoveg = Text(root, height=10, width=100, font=("Arial", 25))
       szoveg.pack(pady=10)
       szoveg.insert("end", "Ez egy szöveg mező.")

    def create_buttons(self):
        for i in self.szintek:
                button = CustomButton(self.master, text=f"{i}", font=("diediedie", 30))
                button.pack(pady=5)

root = tk.Tk()
app = MyApp(root)
root.mainloop()
