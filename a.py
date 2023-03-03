import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import json

with open('kartyak.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self['command'] = self.on_button_click

    def on_button_click(self):
        szoveg.configure(state='normal')
        szoveg.delete(1.0, END)
        e = int(self['text'])
        szöveg= data[e-1]["szoveg"]
        szoveg.insert("end", f'{szöveg}')
        
        
        #szoveg.configure(state='disabled')

szintek = [1, 2, 3, 4,]
class App:
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
        frame = Frame(root)
        frame.pack(side=TOP, pady=10,)

        for i in self.szintek:
            button = CustomButton(frame, text=i, font=("diediedie", 30), fg="#000000", width=5, height=2)
            button.pack(side=LEFT, padx=20, pady=20)

root = tk.Tk()
app = App(root)
root.mainloop()
