gastos = 3
patos = 4
gansos = 2

total_patas = 44

patas_gato = 4
patas_pato = 2
patas_ganso = 2
patas_cordero = 4

patas_sin_corderos = (gastos * patas_gato) + (patos * patas_pato) + (gansos * patas_ganso)

patas_corderos = total_patas - patas_sin_corderos

corderos = patas_corderos // patas_cordero

print("hay", corderos, "Corderos en clase")