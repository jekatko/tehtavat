import random

# Arvotaan luku vain kerran
salaisuus = random.randint(1, 10)
while True:
    syote = input("Arvaa luku väliltä 1–10: ")
    # Varmistetaan, että syöte on kokonaisluku
    try:
        arvaus = int(syote)
    except ValueError:
        print("Anna kokonaisluku.")
        continue

    if arvaus < salaisuus:
        print("Liian pieni arvaus.")
    elif arvaus > salaisuus:
        print("Liian suuri arvaus.")
    else:
        print("Oikein!")
        break
