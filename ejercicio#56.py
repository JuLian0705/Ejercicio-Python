def minimo_de_bolitas_para_repetir():
    colores = {
        "rojas": 2,
        "azules": 3,
        "blancas": 10,
        "verdes": 4,
        "negras": 3
    }

    total_colores = len(colores)
    minimo_para_repetir = total_colores + 1
    
    print("Colores de bolitas en el saco:")
    for color, cantidad in colores.items():
        print(f"{color.capitalize()}: {cantidad} bolitas")

    print("\nPara garantizar que almenos dos bolitas sean del mismo color")
    print(f"Se deben sacar al menos  {minimo_para_repetir} bolitas")

minimo_de_bolitas_para_repetir()