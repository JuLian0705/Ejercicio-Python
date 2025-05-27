n = 5

cubo = [[[1 for _ in range(n)] for _ in range(n)] for _ in range(n)]

cubo[0][0][0] = 0  # esquina
cubo[1][2][3] = 0
cubo[4][4][4] = 0
cubo[2][2][2] = 0
cubo[3][0][1] = 0

total_original = n * n * n
cubos_restantes = sum(sum(sum(layer for layer in fila) for fila in plano) for plano in cubo)
cubos_sacados = total_original - cubos_restantes

print(f"Total de cubos en el cubo original: {total_original}")
print(f"Cubos que permanecen: {cubos_restantes}")
print(f"Cubos que se han sacado: {cubos_sacados}")
