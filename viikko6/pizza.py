import math

def pizzan_yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 2) / 100  # cm → m
    pinta_ala = math.pi * (sade_m ** 2)
    return hinta / pinta_ala

# Pääohjelma
print("Anna kahden pizzan tiedot.")

halkaisija1 = float(input("1. pizzan halkaisija (cm): "))
hinta1 = float(input("1. pizzan hinta (€): "))

halkaisija2 = float(input("2. pizzan halkaisija (cm): "))
hinta2 = float(input("2. pizzan hinta (€): "))

yks1 = pizzan_yksikkohinta(halkaisija1, hinta1)
yks2 = pizzan_yksikkohinta(halkaisija2, hinta2)

print(f"1. pizzan yksikköhinta: {yks1:.2f} €/m²")
print(f"2. pizzan yksikköhinta: {yks2:.2f} €/m²")

if yks1 < yks2:
    print("1. pizza on parempi vastine rahalle.")
else:
    print("2. pizza on parempi vastine rahalle.")
