import json

# Fájl beolvasása
with open('kartyak.json', 'r') as f:
    kartyak = json.load(f)
e = 1
# JSON adatok feldolgozása
szint = kartyak[e-1]["sorszam"]
szoveg = kartyak[e-1]["szoveg"]
akcio = kartyak[e-1]["akcio"]
    
    # Kártya adatainak felhasználása
print('\n')
print(f"SZINT {szint}: {szoveg}")
print(f"Akció: {akcio}\n")
