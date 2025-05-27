import math

class Pieza:
    def __init__(self, tipo, area):
        self.tipo = tipo
        self.area = area

cuadrado_pequeño = Pieza("Cuadrado Pequeño", 1)
triangulo = Pieza("Triángulo", 2)

pajaro = [
         cuadrado_pequeño,
            triangulo,
            triangulo,
            triangulo
         ]

area_total = sum(p.area for p in pajaro)
print(f"El área total del pájaro es: {area_total}")