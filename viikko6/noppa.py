import random

def heita_noppaa():
    return random.randint(1, 6)

# Pääohjelma
while True:
    silmaluku = heita_noppaa()
    print("Heitit:", silmaluku)
    if silmaluku == 6:
        break
