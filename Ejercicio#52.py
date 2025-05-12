total_libros = 10
media_total = 275
paginas_primer_libro = 185

total_paginas = total_libros * media_total

paginas_restantes = total_paginas - paginas_primer_libro

media_otros_nueve = paginas_restantes / (total_libros - 1)

print(f"La media de páginas de los otros 9 libros es: {media_otros_nueve}")
