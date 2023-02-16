import random
import keyboard
import json


def DoboKocka():
    dobas = random.randint(1,6)
    return dobas


class Tomó:
    def __init__(self, nev, ugyesseg, eletero, szerencse, depresszio, inventory, arany, liquid, csillogo, kaja):
        self.nev = nev
        self.ugyesseg = DoboKocka() + 6
        self.eletero = DoboKocka() + DoboKocka() + 12
        self.szerencse = DoboKocka() + 6
        self.depresszio = 0
        self.inventory = 'Vaskard', 'Bőrvért'
        self.arany = arany
        self.liquid = liquid
        self.csillogo = csillogo
        self.kaja = kaja

class Enemy:
    def __init__(self, nev, ugyesseg):
        pass
        self.name = nev
        self.ugyesseg = DoboKocka + DoboKocka 
        self.eletero = DoboKocka + DoboKocka 