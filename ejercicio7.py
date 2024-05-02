
Frutas_diccionario={"platano":1.35,
                     "manzana":0.80,
                     "pera":0.85,
                     "naranja":0.70}

for n in range (4):
        input_fruta =  input("Introduzca el nombre de la fruta:")
        input_kg = input("Introduzca el número de Kg:")
        Frutas_diccionario[input_fruta] = input_kg


        

print (Frutas_diccionario)        


