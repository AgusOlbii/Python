"""
Funciones: Son bloques de codigos que ralizan una tarea especifica. 
            Son usados en la programacion porque permiten
            reutilizar el codigo.
Estructura
de Datos:  Las estructuras de datos permiten
            organizar los datos de tal forma
            que su manipulacion sea mas
            sencilla
"""
#Funciones sin Parametros!
def saludar():
    print("Hola Mundo!")
#saludar()

def suma():
    print(f"La suma es: {6+6}")
#suma()

#Funciones con Parametros!
"""
Los parametros son valores que enviamos cuando invocamos la funcion
y permiten realizar operaciones dentro de la funcion. 
"""
#Primer Ejemplo:
def es_par(numero): #Aca "numero" es un parametro de la funcion
    if numero % 2 == 0:
        print(f"el numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
es_par(5) #Aca el 5 es un argumento que le pasamos a la funcion y lo recibe como parametro

#Segundo Ejemplo:
def programador(nombre):
    print("Hola " + nombre + " eres muy bueno en tu trabajo!")
    
programador("agustin")

#Tercer Ejemplo:
def resta(a = None, b = None): #En este caso los parametros les estamos asignando un valor por defecto, en caso que el usuario no introduzca ningun valor
    if a == None or b == None:
        print("Error! debes enviar dos numeros a la funcion!")
        return
    return a-b
resultado = resta(5, 2)
if resultado != None:
    print(resultado)
    
#Tercer Ejemplo:
def multiplicacion(numero = None):
    if numero == None:
        print("Por favor introduce un numero!")
    else:
        print(f"Tabla de multiplicar del {numero}")
        for i in range(10):
            print(f"{i+1} x {numero} = {(i+1)*numero}")
multiplicacion(5)


#Funciones con parametros posicionales
"""
En los lenguajes de programacion de alto nivel, al declarar una funcion
podemos definir una serie de parametros con los que invocar a dicha funcion. 
Pero por regla general, el numero y el nombre de estos parametros es inmutable. 
"""
# *args
"""
Se usan para pasar de forma opcional distintos valores. 
Son convencion, por lo que puede ir otro nombre, pero el * si es necesario. 
"""
def datos_usuario(*args):
    print(args)
datos_usuario("Paola", "Ramirez", 24, "Cra56#4-00", "Cartagena") #Devuelve una tupla.


# **kwargs
"""
Se les llama asi por convencion. 
Se usan para pasar distintos valores con la diferencia
de que las variables tienen un nombre. 
Es recomendable usarlo cuando se trabaja con base de datos,
sobre todo para filtrar la informacion. 
"""
def info_usuarios(**kwargs):
    print(kwargs)

info_usuarios(nombre = "Paola", apellido = "Ramirez", edad= 24, direccion = "Cra56#4-00", ciudad= "Cartagena")



#Primer Ejemplo:
def suma1(*args):
    aux = 0
    for arg in args:
        aux += arg
    return aux
resultado1 = suma1(1,2,3,4,5,6,7,8,9)
print(resultado1)
"""
Este primer ejemplo remplazaria lo siguiente:
---------------------------------------------------------------
def resta(a = None, b = None): #En este caso los parametros les estamos asignando un valor por defecto, en caso que el usuario no introduzca ningun valor
    if a == None or b == None:
        print("Error! debes enviar dos numeros a la funcion!")
        return
    return a-b
resultado = resta(5, 2)
if resultado != None:
    print(resultado)
----------------------------------------------------------------
Este primer ejemplo nos otorga la posibilidad de pedirle a la funcion que nos sume la cantidad de numeros que querramos pasarle como argumentos,
en cambio, este codigo nos limita a poder pasarle solamente dos numeros. 
"""

#Segundo Ejemplo:
def lenguaje(nombre, *lenguajes):
    print(f"Hola {nombre}")
    print(f"Tus lenguajes favoritos son: {lenguajes}") #En este caso, lenguajes estaria remplazando args, esto es posible ya que args se utiliza
                                                        #unicamente por convencion. 
lenguaje("Agustin", "Python", "SQL")

def idioma(nombre, **kwargs):
    print(f"Hola {nombre}")
    print("Buscando informacion acerca de tus lenguajes favoritos...")
    print(f"informacion: ")
    contador = 0
    for clave in kwargs:
        contador += 1
        print(f"Tu {contador} lenguaje favorito es: {kwargs[clave]}")
        
idioma("Agustin", idioma1 = "Español", idioma2 = "Ingles")