import tkinter as tk
import json
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import json

with open('kartyak.json', 'r', encoding='utf-8') as f:
        szintek = json.load(f)
root = tk.Tk()

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalandjáték")
        self.master.configure(background="#261401")
        self.szint_szovegek()

    def szint_szovegek(self):
       global szoveg
       szoveg = tk.Text(root, height=10, width=100, font=("Arial", 25))
       szoveg.pack(pady=10)
       szoveg.insert("end", "Ez egy szöveg mező.")

    def create_buttons(self, szint):
        global szintek
        frame = tk.Frame(root)
        frame.pack(side=tk.TOP, pady=10)

        for i in range(len(szintek[szint]["ugras"])):
            button = tk.Button(frame, text=i+1, font=("diediedie", 30), fg="#000000", width=5, height=2, command=lambda i=i: self.on_button_click(szint, i))
            button.pack(side=tk.LEFT, padx=20, pady=20)

    def on_button_click(self, szint, i):
        szoveg.configure(state='normal')
        szoveg.delete(1.0, tk.END)
        szöveg = szintek[szint]["ugras"][i]["szoveg"]
        szoveg.insert(tk.END, f'{szöveg}')
        if szintek[szint]["ugras"][i]["akcio"]["tipus"] == "ugrás":
            ugras = szintek[szint]["ugras"][i]["akcio"]["ugras"]
            self.master.destroy()
            self.master = tk.Tk()
            app = App(self.master)
            app.create_buttons(ugras)
            self.master.mainloop()



    root = tk.Tk()
    app = App(root)
    app.create_buttons(0)
    root.mainloop()
