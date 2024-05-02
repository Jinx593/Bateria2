import string

#obtenemos las letras del abecedario
palabra = "espantapajaros"
abecedario = string.ascii_letters[:26]

#declaramos un diccionario vacio y lo pupulamos
dict_letra_a_entero = dict()
for n in range (len(abecedario)): 
    dict_letra_a_entero[abecedario[n]]=n

#con este diccionario se implementa de forma sencilla la logica de 
for letra in palabra: 
    numero= dict_letra_a_entero[letra]
    print (letra, numero) 

#print(dict_letra_a_entero)

#abecedario = ['a','b','c','d',]