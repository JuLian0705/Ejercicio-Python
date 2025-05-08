planta_baja = 0
segundo_sotano = -2
piso_maria = 7

bajada = abs(segundo_sotano - planta_baja)
subida = abs(piso_maria - planta_baja)

total_pisos = bajada + subida

print(f"Maria recorrio un total de {total_pisos} pisos")