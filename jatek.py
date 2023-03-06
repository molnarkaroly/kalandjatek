import random
import keyboard
import json
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import json



with open('kaland.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

k = -1
vege = False
while not vege:  

    cim = data["cim"]
    bevezeto = data["bevezeto"]
    ugrasss = data["kartyak"][0]["szoveg"]
    akcio = data["kartyak"][k]['akcio']
    print(akcio)

def DoboKocka():
    dobas = random.randint(1,6)
    return dobas


class Harcos:
    def __init__(self, nev, ugyesseg, eletero, szerencse, depresszio, inventory, arany, liquid, csillogo, kaja):
        self.nev = nev
        self.ugyesseg = DoboKocka() + 6
        self.eletero = DoboKocka() + DoboKocka() + 12
        self.szerencse = DoboKocka() + 6
        self.depresszio = 0
        self.inventory = inventory['Vaskard', 'Bőrvért']
        self.arany = arany
        self.liquid = liquid
        self.csillogo = csillogo
        self.kaja = kaja 


    def harc(self, enemy):
        while self.health > 0 and enemy.health > 0:
            sebzes = 2
            enemy.health -= sebzes
            if enemy.health <= 0:
                print(f"{self.name} nyert a harcban.")
                szoveg = (f'1: {"ugras"[1]}')
                if len('ugras') > 1:
                    szoveg = (f'1: {data["ugras"][1]} 2:{ ["ugras"][2]}' )
                break
            self.health -= enemy.sebzes
            if self.health <= 0:
                print(f"{enemy.name} nyert játékod is véget ért")
                szoveg = (f"{enemy.name} nyert játékod is véget ért")
                break



    def ugyessegm(self):
        self.ugyesseg = self.ugyesseg + ugyessegm

    def ugyessegn(self):
        self.ugyesseg = self.ugyesseg + ugyessegn

    def eleterom(self):
        self.eletero = self.eletero + eleterom

    def eleteron(self):
        self.eletero = self.eletero - eleteron

    def szerencsem(self):
        self.szerencse = self.szerencse + szerencsem

    def fix(self):
        if fix == True:
            self.szerencse < 6
            self.szerencse = 6


    def halál(self):
        szöveg = " Játékod itt véget ért meghaltál XDDDDDDDDDDDD (sz@r lehet)"


class Enemy:
    def __init__(self, nev, ugyesseg, eletero, sebzes = 2):
        self.name = data["harc"][0]
        self.ugyesseg = data["harc"][1]
        self.eletero =  data["harc"][3]
        self.sebzes = sebzes

    def probaszerencse(self, szerencse):
        if DoboKocka() + DoboKocka() <= self.szerencse:
            probaszerencsee = True
            self.szerencse -= 1
            self.sebzes = 1
        else:
            probaszerencsee = False
            self.szerencse -= 1


                                                                #innentől karcsi dolga "DO NOT ENTER"

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self['command'] = self.on_button_click

    def on_button_click(self):
        print(int(self['text']))
        szint = int(self['text'])

bevezeto= data["bevezeto"]
szöveg  = "Szeretném közölni a játékossal, hogy ez a játék Tomó halálával végződik legtöbb esetben csak erős tűrőképességel bíróknak ajánljuk ezt a tartalmat."
szintek = [1,5,6]

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalandjáték")
        self.master.configure(background="#261401")
        self.szintek = szintek

        self.szint_szovegek()
        self.create_buttons()

    def szint_szovegek(self):
       text = Text(root, height=10, width=100,font=("Arial", 25))
       text.pack(pady=10)
       text.insert("end", szöveg)

    def create_buttons(self):
        for i in self.szintek:
                button = CustomButton(self.master, text=f"{i}",font=("Arial", 30))
                button.pack(pady=5)

root = tk.Tk()
app = MyApp(root)
root.mainloop()

