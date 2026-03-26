lista = []

while True:
    arvo = int(input("Uusi arvo: "))

    if arvo == 0:
        print("Hei hei!")
        break

    lista.append(arvo)

    print("Lista nyt:", lista)
    print("Lista järjestyksessä:", sorted(lista))
