import os

f = open('metin.txt', 'r')

metin = f.read()

kelimeler = metin.split()
kelime_sayaci = {}

for kelime in kelimeler:
    kelime = kelime.strip('.,!?()[]{}":;')
    kelime = kelime.lower()

    if kelime in kelime_sayaci:
        kelime_sayaci[kelime] += 1
    else:
        kelime_sayaci[kelime] = 1


for kelime, sayac in kelime_sayaci.items():
    print(f"{kelime}: {sayac} kez")