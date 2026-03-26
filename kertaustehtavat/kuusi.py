def kuusi(koko):
    print("Tämä on kuusi!")

    leveys = 2 * koko - 1  # kuusen alin leveys

    # Kuusen oksat
    for i in range(1, koko + 1):
        tahtia = 2 * i - 1
        print(("*" * tahtia).center(leveys))

    # Rungon tähti
    print("*".center(leveys))
kuusi(5)
