def encontrar_fresas():
    for x in range(1, 100):
        for f in range(1, 100):
            usted = x + f
            margarita = x - f
            if usted == margarita + 10:
                print(f"Ambos tenian inicialmente {x} y {f} fresas")
                print(f"Margarita tiene que darle {f} fresas para que usted tenga 10 más que ella.")
                return
encontrar_fresas()