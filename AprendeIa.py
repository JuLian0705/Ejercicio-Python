import random

def suma_real(a, b):
    return a + b

def ia_suma(a, b, conocimiento):
    key = (a, b)
    if key in conocimiento:
        return conocimiento[key]
    else:
        return random.randint(a + b - 3, a + b + 3)
    
conocimiento = {}
intentos = 0

for i in range(10):
    print(f"\nEjercicio {i + 1}")
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    predicion = ia_suma(a, b, conocimiento)
    real = suma_real(a, b)

    print(f"Ia intenta sumar: {a} + {b} = {predicion}")

    if predicion == real:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta es: {real}")
        conocimiento[(a, b)] = real

    intentos += 1

print("\nResumen del conocimiento aprendido por la IA:")
for clave, valor in conocimiento.items():
    print(f"{clave[0]} + {clave[1]} = {valor}")
