
#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#passed = []

asignatura_dict = {"matematicas": None,
                   "fisica": None,
                   "Quimica":None,
                   "Historia":None,
                   "Lengua": None,
                   }
#bucle que recorre la Lista de asignaturas
for subject in asignatura_dict:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))

    asignatura_dict[subject]= score

#bucle for de las asignaturas aprobadas
#Elimina las asignaturas aprobadas    
    asignatura_dict.remove(subject)
#Muestra las asignaturas que no superan el 5 por lo tanto no estan aprobadas    
print("Tienes que repetir " + str(asignatura_dict))