from datetime import datetime, timedelta

valor_nominal = 120000
tasa_descuento = 0.10

fecha_emision = datetime.strptime("2025-07-15", "%Y-%m-%d")
plazo_dias = 150
fecha_vencimiento = fecha_emision + timedelta(days=plazo_dias)

fecha_venta = datetime.strptime("2025-10-01", "%Y-%m-%d")

dias_restante = (fecha_vencimiento - fecha_venta).days
valor_presente = valor_nominal / (1 + tasa_descuento * dias_restante / 360)

print(f"fecha de vencimiento: {fecha_vencimiento.date()}")
print(f"Dias restantes desde el 20 de octubre:", dias_restante)
print("Valor Actual de pagare (lo que recibe el inversionista): ${:,.2f}".format(valor_presente))
