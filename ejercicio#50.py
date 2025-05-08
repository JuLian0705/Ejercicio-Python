meses_verano = 3
meses_resto = 12 - meses_verano

ocupacion_verano = 92
ocupacion_resto = 40

ocupacio_total = (meses_verano * ocupacion_verano + meses_resto * ocupacion_resto) / 12
print(f"El porcentaje de ocupación total es: {ocupacio_total:.2f}%")