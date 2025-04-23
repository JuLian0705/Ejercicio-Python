def gatos_necesarios(ratones_total, tiempo_total, gasto_base=5, ratones_base=5, tiempo_base=5):
    ratones_por_gato_por_tiempo =  ratones_base / gasto_base

    ratones_por_gato_total = (ratones_por_gato_por_tiempo / tiempo_base) * tiempo_total
    gatos_necesarios = ratones_total / ratones_por_gato_total

    return int(gatos_necesarios) 

ratones = 100
tiempo = 100

print(f"Se necesitan {gatos_necesarios(ratones, tiempo)} gatos para cazar {ratones} ratones en {tiempo} minutos.")