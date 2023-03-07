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


e = 1

vege = False

#cim = data["Cards"]["cim"]
#bevezeto = data["Cards"]["bevezeto"]
#ugrasss = data["Cards"][0]["szoveg"]
#akcio = data["Cards"][e]['akcio']
#print(akcio)

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
        self.inventory = inventory
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
        self.eletero = self.eletero - data["Cards"][e-1]["akció"]["minushp"]

def eletero2(self):
        self.eletero = self.eletero +  data["Cards"][e-1]["akció"]["plushp"]

def szerencsem(self):
        self.szerencse = self.szerencse - data["Cards"][e-1]["akció"]["minusluck"]

def sebzesplus(sebzes):
    return 3

def fix(self):
        if fix == True:
            self.szerencse < 6
            self.szerencse = 6





class Enemy:
    def __init__(self, nev, ugyesseg, eletero, sebzes = 2):
        self.name = data["Cards"][e-1]["akció"]["ellenfél"][0]
        self.ugyesseg = data["Cards"][e-1]["akció"]["ellenfél"][1]
        self.eletero =  data["Cards"][e-1]["akció"]["ellenfél"][2]
        self.sebzes = sebzes



def vane(ebben,ez):
    for i in (ebben):
        if ez == i:
            return True
        else:
            return False
        
def halál(vege):
   print(" Játékod itt véget ért meghaltál XDDDDDDDDDDDD (bibis lett az ujjad és meghaltál) ")
   return  True

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
    
e= 2

print(data["Cards"][e-1]["szint"])
print (data["Cards"][e-1]["szöveg"])
szint = int(input("Szint: ")) 
if szint != data["Cards"][e-1]["akció"]["ugrás"]:
    halál(vege)
else:
    
 szint = e

 while not vege:  
    if keyboard.is_pressed("Escape"):
       vege= True


    e = szint
   

    if data["Cards"][e-1]["akció"]["tipus"] =="halál":
        halál(vege)
        break

    if data["Cards"][e-1]["akció"]["tipus"] =="ugrás":
        ugrasss= data["Cards"][e-1]["akció"]["ugrás"]
        print(f'merre mész tovább {ugrasss}')
        print(data["Cards"][e-1]["szöveg"])
        print(f'amerre tovább mehetsz: {ugrasss}')
        tszint= int (input("Melyikre mész tovább?")) #tszint talán szint azt ellenőrzi hogy van e olyan szint a listában
        if vane(ugrasss,tszint)== True:
            szint = tszint
        else:
            print("nincs ilyen szint")
            halál(vege)

    if data["Cards"][e-1]["akció"]["tipus"] =="harc":
        harc(Tomó, data["Cards"][e-1]["akció"]["harc"])
        continue

    if data[e-1]["akció"]["választás"]:
        ugrasss= data[e-1]["akció"]["ugrás"]
        print(f'merre mész tovább {ugrasss}')
        tszint= int (input("Melyikre mész tovább?")) #tszint talán szint azt ellenőrzi hogy van e olyan szint a listában
        if vane(tszint,ugrasss)== True:
            szint = tszint
        else:
            print("nincs ilyen szint")
            continue

    if data["Cards"][e-1]["akció"]["tipus"]=="luckválasztás":
        if probaszerencse() == True:
            szint= data["Cards"][e-1]["akció"]["ugrás"][0]
        else:
            szint= data["Cards"][e-1]["akció"]["ugrás"][1]
    
    if data["Cards"][e-1]["akció"]["tipus"]=="győzelem":
        print("Győztél!!! nyisd meg ezt a linket")
        print("https://media.giphy.com/media/ZcUGu59vhBGgbBhh0n/giphy.gif")

    if data["Cards"][e-1]["akció"]["tipus"]=="tválasztás":
        if vane(data["Cards"][e-1]["akció"]["tárgyválasztaás"],inventory)== False:
            tszint = data["Cards"][e-1]["akció"]["ugrás"][0]

            
        else:
            tszint = data["Cards"][e-1]["akció"]["ugrás"][1]
            continue






    



