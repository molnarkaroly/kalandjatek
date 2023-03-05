import json

# Fájl beolvasása
with open('kartyak.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
e = 2
# JSON adatok feldolgozása
szint = data[e-1]["sorszam"]
szoveg = data[e-1]["szoveg"]
akcio = data[e-1]["akcio"]
    
    # Kártya adatainak felhasználása
print('\n')
print(f"SZINT {szint}: \n {szoveg}")
print(f"Akció: {akcio}\n")

if akcio["tipus"]=="ugrás":
    print(f'ugras:{data[e-1]["akcio"]["ugras"]}')
