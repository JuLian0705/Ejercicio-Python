horas_dormidas = 20
horas_totales = 24  

horas_despierto = horas_totales - horas_dormidas

consumo_por_hora = 50

gramos_comidos = horas_despierto * consumo_por_hora

print(f"Koko comio", gramos_comidos, "gramos de hojas ayer")