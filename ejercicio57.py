precio_choclo = 200
personas = 4
choclos_por_persona = 4

total_choclos = personas * choclos_por_persona

choclos_gratis = total_choclos // 6
chclos_pagados = total_choclos - choclos_gratis

total_pegado = chclos_pagados * precio_choclo

print(f"Total de choclos comprados: {total_choclos}")
print(f"Choclos gratis obetenidos: {choclos_gratis}")
print(f"Choclos que se pagaron: {chclos_pagados}")
print(f"Total pagado: {total_pegado} pesos. ")