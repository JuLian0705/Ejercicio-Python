contador = 0

for a in range (1, 10):
    for b in range(0, 10):
        if abs(a - b) == 3:
            for c in range(0, 10):
                if abs(b - c) == 3:
                    print(f"{a}{b}{c}")
                    contador += 1
                    
print(f"Total de números encontrados: {contador}")
