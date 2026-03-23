import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

# Pääohjelma
tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

while True:
    silmaluku = heita_noppaa(tahkojen_maara)
    print("Heitit:", silmaluku)
    if silmaluku == tahkojen_maara:
        break
