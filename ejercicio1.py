"""
algoritmo para el calculo del año bisiesto
"""

def bisiesto(año):
    es_bisiesto = False
    if año % 4 == 0: # Paso 1
        if año % 100 == 0: # Paso 2
            if año % 400 == 0: # Paso 3
                es_bisiesto = True

    else:
        es_bisiesto = False # Paso 5


    return es_bisiesto
if bisiesto(2024):
    print ("es_bisiesto")

