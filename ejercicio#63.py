from sympy import symbols, Eq, solve
t = symbols('t')

equacion = Eq((8 + 8*t) / (2 + t), 5)

solucion = solve(equacion, t)
if solucion:
    tiempo_corriendo = solucion[0]
    print(f"Ana debe correr durante {tiempo_corriendo} horas.")
else:
    print("No hay solucion.")