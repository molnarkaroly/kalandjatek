import random
import keyboard
import json


def DoboKocka():
    dobas = random.randint(1,6)
    return dobas

ugras= []

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

    def harc(self, enemy ):
        while self.health > 0 and enemy.health > 0:
            enemy.health -= self.strength
            if enemy.health <= 0:
                print(f"{self.name} nyert a harcban.")
                szoveg = (f'1: {ugras[1]}')
                if len(ugras) > 1:
                    szoveg = (f'1: {ugras[1]} 2:{ ugras[2]}' )
                break
            self.health -= enemy.strength
            if self.health <= 0:
                print(f"{enemy.name} nyert játékod is véget ért")
                szoveg = (f"{enemy.name} nyert játékod is véget ért")
                break

class Enemy:
    def __init__(self, nev, ugyesseg):
        pass
        self.name = nev
        self.ugyesseg = DoboKocka + DoboKocka 
        self.eletero = DoboKocka + DoboKocka 

    