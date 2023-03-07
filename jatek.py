import random
import keyboard
import json
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import json



with open('szöveg.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

szint = data["szint"]
e = szint

vege = False

cim = data["cim"]
bevezeto = data["bevezeto"]
ugrasss = data["kartyak"][0]["szoveg"]
akcio = data["kartyak"][e]['akcio']
print(akcio)

def DoboKocka():
    dobas = random.randint(1,6)
    return dobas

inventory= ['Vaskard', 'Bőrvért']
arany= 0
liquid= 5
csillogo= 1
kaja= 5
class Harcos:
    def __init__(self, nev): #ugyesseg, eletero, szerencse, depresszio, inventory, arany, liquid, csillogo, kaja
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


    
Tomó= Harcos("Tomó")



def ugyessegm(self):
        e = szint
        self.ugyesseg = self.ugyesseg 

def ugyesseg1(self): 
        self.ugyesseg = self.ugyesseg + ugyesseg1


def ugyessegn(self):
        self.ugyesseg = self.ugyesseg + ugyessegn
def ugyesseg2(self):
        self.ugyesseg = self.ugyesseg + ugyesseg2

def eleterom(self):
        self.eletero = self.eletero + eleterom
def eletero1(self):
        self.eletero = self.eletero + eletero1

def eleteron(self):
        self.eletero = self.eletero - eleteron
def eletero2(self):
        self.eletero = self.eletero - eletero2

def szerencsem(self):
        self.szerencse = self.szerencse + data[e-1]["+luck"]

def szerencsem(self):
        e = szint
        self.szerencse = self.szerencse - data[e-1]["-luck"]

def fix(self):
        if fix == True:
            self.szerencse < 6
            self.szerencse = 6





class Enemy:
    def __init__(self, nev, ugyesseg, eletero, sebzes = 2):
        self.name = data["harc"][0]
        self.ugyesseg = data["harc"][1]
        self.eletero =  data["harc"][3]
        self.sebzes = sebzes


e = szint

def vane(ebben,ez):
    for i in (ebben):
        if ez == i:
            return True
        else:
            return False
        
def halál(self):
    szöveg = " Játékod itt véget ért meghaltál XDDDDDDDDDDDD (sz@r lehet)"
    vege= True

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

def probaszerencse(Tomó, szerencse):
    if DoboKocka() + DoboKocka() <= Tomó.szerencse:
        Tomó.szerencse -= 1
        Tomó.sebzes = 1
        return True

    else:
        Tomó.szerencse -= 1
        return False    

while not vege:  
    print("data[e-1]["kartyak"]["szint"]")
    print (data[e-1]["szöveg"])

    if data[e-1]["akcio"] ==["halál"]:
        halál()
        continue

    if data[e-1]["akció"]["tipus"] ==["ugrás"]:
        ugrasss= data[e-1]["akcio"]["ugrás"]
        print(f'merre mész tovább {len(ugrasss)}')
        tszint= int (input("Melyikre mész tovább?")) #tszint talán szint azt ellenőrzi hogy van e olyan szint a listában
        if vane(tszint,ugrasss)== True:
            szint = tszint
        else:
            print("nincs ilyen szint")
            continue

    if data[e-1]["akció"]["tipus"] ==["harc"]:
        harc(Tomó, data[e-1]["akció"]["harc"])
        continue

    #if data[e-1]["akció"]["választás"]:
    #    ugrasss= data[e-1]["akcio"]["ugrás"]
    #    print(f'merre mész tovább {len(ugrasss)}')
    #    tszint= int (input("Melyikre mész tovább?")) #tszint talán szint azt ellenőrzi hogy van e olyan szint a listában
    #    if vane(tszint,ugrasss)== True:
    #        szint = tszint
    #    else:
    #        print("nincs ilyen szint")
    #        continue

    if data[e-1]["tipus"]=="luckválasztás":
        if probaszerencse() == True:
            szint= data[e-1]["akcio"]["ugrás"][0]
        else:
            szint= data[e-1]["akcio"]["ugrás"][1]
    
    if data[e-1]["tipus"]=="győzelem":
        print("Győztél!!! nyisd meg ezt a linket")
        print("https://media.giphy.com/media/ZcUGu59vhBGgbBhh0n/giphy.gif")

    if data[e-1]["tipus"]=="tválasztás":
        if vane(data[e-1]["cards"]["akcio"]["tárgyválasztaás"],inventory)== False:
            tszint = data[e-1]["Cards"]["akcio"]["ugrás"][0]
            
        else:
            tszint = data[e-1]["akcio"]["ugrás"][1]
            continue





    



