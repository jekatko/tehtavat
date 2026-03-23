def poista_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

# Pääohjelma
luvut = [1, 2, 3, 4, 5, 6, 7]
karsittu = poista_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Parilliset luvut:", karsittu)
