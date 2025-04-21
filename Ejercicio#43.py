def caballo_acertijo():
    print("Adivina")
    print("Un caballo esta atado a una cuerda de 20 pies")
    print("El agua esta a 30 pies de distancia, pero el caballo llega facilmente y bebe agua")
    print("¿Como es esto posible?")

    intentos = 3
    while intentos > 0:
        respuesta = input("\nTu respuesta: ").strip().lower()

        if "no está atada" in respuesta or "la cuerda no está atada" in respuesta or "no está amarrada" in respuesta:
            print("\n✅ ¡Correcto! La cuerda no está atada a nada, así que el caballo puede moverse libremente.")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"\n❌ Incorrecto. Te quedan {intentos} intentos.")
            else:
                print("\n❌ Incorrecto. Has agotado tus intentos.")
                print("La respuesta correcta es: La cuerda no está atada a nada, así que el caballo puede moverse libremente.")

caballo_acertijo()