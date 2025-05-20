from itertools import permutations

digitos = '2013'
perms = set(int(''.join(p)) for p in permutations(digitos) if p[0] != '0')

numeros = sorted(perms)

diferencias = [b - a for a, b in zip(numeros, numeros[1:])]

diferencia_maxima = max(diferencias)

print("numeros generados:", numeros)
print("Diferencias entre vecinos:", diferencias)
print("La diferenci mas grande entre vecinos es: ", diferencias)
