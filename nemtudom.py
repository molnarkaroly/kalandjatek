import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import json

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self['command'] = self.on_button_click

    def on_button_click(self):
        global eletero_szint, harci_ero_szint, ugyessegi_szint
        eletero_szint += 5
        harci_ero_szint += 3
        ugyessegi_szint += 2
        eletero_label.configure(text=f"Életerő: {eletero_szint}")
        harci_ero_label.configure(text=f"Harci erő: {harci_ero_szint}")
        ugyessegi_szint.configure(text=f"Ügyességi szint: {ugyessegi_szint}")

    szintek = [15, 65, 48]
    eletero_szint = 100
    harci_ero_szint = 50
    ugyessegi_szint = 30

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalandjáték")
        self.master.configure(background="#261401")
        self.szintek = CustomButton.szintek

        self.szint_szovegek()
        self.create_buttons()
        self.szint_label()

    def szint_szovegek(self):
        global szoveg, eletero_label, harci_ero_label, ugyessegi_label
        szoveg = Text(root, height=10, width=100, font=("Arial", 25))
        szoveg.pack(pady=10)
        szoveg.insert("end", "Ez egy szöveg mező.")

        eletero_label = Label(root, text=f"Életerő: {CustomButton.eletero_szint}", font=("Arial", 20))
        eletero_label.pack()

        harci_ero_label = Label(root, text=f"Harci erő: {CustomButton.harci_ero_szint}", font=("Arial", 20))
        harci_ero_label.pack()

        ugyessegi_label = Label(root, text=f"Ügyességi szint: {CustomButton.ugyessegi_szint}", font=("Arial", 20))
        ugyessegi_label.pack()

    def create_buttons(self):
        for i in self.szintek:
            button = CustomButton(self.master, text=f"     {i}     ", font=("diediedie", 30))
            button.pack(pady=5)

    def szint_label(self):
        szint_label = Label(root, text="Szintek:", font=("Arial", 20))
        szint_label.pack()

root = tk.Tk()
app = MyApp(root)
root.mainloop()
