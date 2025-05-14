from sympy import symbols, Eq, solve

G, C = symbols('G C')

eq1 = Eq(G, C + 80)
eq2 = Eq(2*G, C + 180)

Solucion = solve((eq1, eq2), (G, C))

print(f"Peso de la canasta: {Solucion[C]} kg")
print(f"Capacidad de un globo: {Solucion[G]} kg")