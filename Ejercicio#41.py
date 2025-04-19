def calcular_cigarrillos(colillas_iniciales):
    cigarros_hechos = 0
    colillas = colillas_iniciales

    while colillas >= 5:
        nuevos_cigarros = colillas // 5
        cigarros_hechos += nuevos_cigarros
        colillas = colillas % 5 + nuevos_cigarros

    return cigarros_hechos

colillas_encontradas = 25
total_cigarros = calcular_cigarrillos(colillas_encontradas)
print(f"Con {colillas_encontradas} colillas se pueden hacer {total_cigarros} cigarros.")