def verificar_cuadrado_positivo(A):
    if A == 0:
        print("A no puede ser cero")
    else:
        resultado = A ** 2
        print(f"A = {A}")
        print(f"A² = {resultado}")
        if resultado > 0:
            print("Como A es positivo, A² > 0, es positivo Se demuestra que el cuadrado de un numero real distinto de cero es positivo")
        else:
            print("Algo esta mal, revisa la logica")

verificar_cuadrado_positivo(5)
verificar_cuadrado_positivo(-3.7)
verificar_cuadrado_positivo(0)