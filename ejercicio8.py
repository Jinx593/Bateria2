cesta_dict = {}

while True: 
    art_nombre = input("introduzca el nombre del articulo:") 
    art_precio = float(input("introduzca el precio del articulo: "))
    n_unidades = int(input)
    cesta_dict[art_nombre] = [art_precio, n_unidades]

print(cesta_dict)
