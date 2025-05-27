personas = {
    "ana": 23,
    "luis": 22,
    "pedro": 19,
    "maria": 30
}

def existe_persona_con_menos_de_21(diccionario):
    for nombre, cantidad in diccionario.items():
        if cantidad <= 20:
            print(f"{nombre} no resolvio mas de 20 problemas ({cantidad})")
            return True

if existe_persona_con_menos_de_21(personas):
    print("Hay al menos una persona que no resolvió más de 20 problemas")
else:
    print("La negación es falsa: Todos resolvieron más de 20 problemas")
