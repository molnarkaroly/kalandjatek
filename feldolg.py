import json

# Fájl beolvasása
with open('kartyak.json', 'r', encoding="utf-8") as f:
    kartyak = json.load(f)
e = 2
# JSON adatok feldolgozása
szint = kartyak[e-1]["sorszam"]
szoveg = kartyak[e-1]["szoveg"]
akcio = kartyak[e-1]["akcio"]
    
    # Kártya adatainak felhasználása
print('\n')
print(f"SZINT {szint}: \n {szoveg}")
print(f"Akció: {akcio}\n")
