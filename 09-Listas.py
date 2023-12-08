"""
Es la estructura mas sencilla que tenemos en python.
Para acceder a cada elemento de la lista utilizamos los indices. 
"""
#Primer Ejemplo:
"""
Escribir un programa que almacene las asignaturas en curso.
"""
materias = ["Matematicas", "Lengua", "Ingles", "Ed. Fisica", "Canto", "Musica", 1, 2, 2, 2, 2]
print(type(materias)) #La funcion type nos devolvera el tipo de dato de la variable.
def mostrar_materias():
    cantidad_materias = len(materias)
    for i in range(cantidad_materias):
        print(materias[i])
mostrar_materias()

print("---------------------")

#print(materias[1])


def agregar_materia():
    materias.append("Java Script") #Se añade un elemento a la lista en la ultima posicion
    return materias

materias = agregar_materia()
mostrar_materias()

print("---------------------")


def eliminar_materia():
    materias.remove("Java Script") #Se elimina el elemento que nombremos
    materias.pop(0) #Elimina el elemento segun su posicion.add()
    del materias[1] #Elimina el elemento segun su posicion. 
    #materias.clear() #Elimina todos los elementos de la lista
    return materias

materias = eliminar_materia()

mostrar_materias()
print("---------------------")


def contador_repeticiones():
    contador = materias.count(2) #Con este METODO .count() veremos cuantas veces aparece un elemento en la lista
    print(contador)
contador_repeticiones()


print("---------------------")


def posicion_materia():
    print(materias.index(2)) #.INDEX nos indica en que posicion de la lista se encuentra el elemento que nombramos.
posicion_materia()



print("---------------------")


def voltear_lista():
    materias.reverse() #.reverse da vuelta la lista
    print(materias)
voltear_lista()
