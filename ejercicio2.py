""" 
carnet por puntos
"""

def carnet (puntos, precio_inicial):
    precio_final_compra = 0 
    descuento = 0
    if puntos < 100:  
        descuento = 0.1
    elif puntos > 100 and puntos < 150:
        descuento = 0.12
    elif puntos == 150:
        descuento = 0.15
    elif puntos > 150:  
        descuento = 0.2
    precio_final_compra = precio_inicial * (1- descuento)

    return precio_final_compra

carnet(100,50) 
precio_final = carnet(106,50)
print(precio_final) 