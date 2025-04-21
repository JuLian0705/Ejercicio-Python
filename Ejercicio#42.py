def medir_un_galon():
    botella_3 = 0
    botella_5 = 0

    pasos = []

    while True:
        botella_3 = 3
        pasos.append("Llenar botella de 3 galones")
        espacio_en_5 = 5 - botella_5
        transferir = min(botella_3, espacio_en_5)
        botella_3 -= transferir
        botella_5 += transferir
        pasos.append(f"Verter {transferir} galones de la botella de 3 a la de 5")

        if botella_3 == 1 or botella_5 == 1:
            pasos.append("¡Listo! Una de las botellas tiene exactamente 1 galón.")
            break

        if botella_3 == 0:
            continue

        if botella_5 == 5:
            botella_5 = 0
            pasos.append("Vaciar la botella de 5 galones")

    for i, paso in enumerate(pasos, 1):
        print(f"Paso {i}: {paso}")

medir_un_galon()
