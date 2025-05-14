def numero_minuto_producto(n):
    if n in [0, 1]: return 10 if n == 0 else 1
    f = []
    for d in range(9, 1, -1):
        while n % d == 0:
            n //= d
            f.append(d)
    return -1 if n > 1 else int(''.join(map(str, sorted(f))))

n = numero_minuto_producto(24)
print(f"Numero: {n}\nSuma de digitos {sum(int(d) for d in str(n))}" if n != -1 else "No existe numero valido")