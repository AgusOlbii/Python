import time
"""
Las agendas telefónicas son una guía donde se encuentran los datos de diferentes personas como su nombre,
domicilio y teléfono. Además, sirven para localizar personas, lugares o servicios. 

Dicho lo anterior, escribamos un programa que permita guardar nombres y números de teléfono.
El programa nos dará el siguiente menú:

1- Consultar: Pide un nombre. Si el nombre se encuentra en la agenda debe mostrar el telefono. 
                Sino indicar que no existe. 
2- Añadir: Pide un nombre. Si el nombre se encuentra en la agenda, indicar que ya existe, sino solicitar
            el numero telefonico.
3- Modificar: Pide un nombre, Si el nombre nombre no esta en la agenda indicar que no existe, sino solicitar
                el nuevo numero de telefono. 
4- Borrar: Pide un nombre, si el nombre no esta en la agenda informar que no existe, sino eliminar el numero
            de telefono. 
5- Salir: Si el usuario digita el numero 5, detener el ciclo.

Los datos para este ejercicio son los siguientes: 
Jose: 302944; Mario: 829455; Angel: 829405 y Luis: 930594.
"""

agenda = {
    "Jose": 302944,
    "Mario": 829455,
    "Angel": 829405,
    "Luis": 930594
}

"""
Con la funcion ingresar_nombre le solicitamos al usuario que introduzca el nombre de la persona
con la que se quiere contactar.
"""
def ingresar_nombre():
    nombre = str(input("Ingrese el nombre que de la persona para ver su numero telefonico:\n"))
    return nombre

"""
Con la funcion verificacion_encontrado podremos verificar que el usuario haya sido encontrado en la agenda y
que nos devuelva tanto el nombre del usuario como si se encontro o no. Para esto se utiliza la funcion
ingresar_nombre
"""
def verificacion_encontrado():
    opc = False
    nombre = ingresar_nombre()
    if nombre in agenda:
        opc = True
    else:
        opc = "El nombre ingresado no existe.\n"
    return opc, nombre
        
"""
La funcion consultar es un poco mas compleja, ya que al usar la funcion verificacion_encontrado,
esta nos retorna dos valores. Esto es posible pero nos los devuelve en forma de tupla, respetando el orden
en el que se escriben al retornarlos. Luego de eso se le asigna a dos variables los valores segun sus posiciones 
y se utiliza un if
"""
def consultar():
    opc_y_nombre = verificacion_encontrado() #tupla
    encontrado = opc_y_nombre[0]#Le asignamos el valor de la posicion 0 de la tupla
    nombre = opc_y_nombre[1]#Le asignamos el valor de la posicion 1 de la tupla
    if encontrado == True:
        print(agenda[nombre] + "\n")
    else:
        print(encontrado + "\n")
        
"""
La funcion añadir utiliza el metodo .update en el diccionario agenda para agregar una key y un valor.
"""
def añadir():
    opc_y_nombre = verificacion_encontrado()
    nombre = opc_y_nombre[1]
    encontrado = opc_y_nombre[0]
    if encontrado == True:
        print("Ese contacto ya existe.\n")
    else:
        nuevo_numero = int(input(f"Ingrese el numero telefonico de {nombre}:\n"))
        agenda.update({nombre: nuevo_numero})
    
"""
En esta funcion es simple. Se verifica que el contacto exista y si es asi se pedira que se ingrese
su nuevo numero telefonico.
"""
def modificar():
    opc_y_nombre = verificacion_encontrado()
    nombre = opc_y_nombre[1]
    encontrado = opc_y_nombre[0]
    if encontrado == False:
        print("El nombre ingresado no existe.\n")
    else:
        nuevo_numero = int(input(f"Ingrese el nuevo numero telefonico de {nombre}:\n"))
        agenda[nombre] = nuevo_numero

"""
En esta funcion se utiliza el metodo del para eliminar un elemento del diccionario.   
"""
def borrar():
    opc_y_nombre = verificacion_encontrado()
    encontrado = opc_y_nombre[0]
    nombre = opc_y_nombre[1]
    if encontrado == True:
        del(agenda[nombre])
    else:
        print("El nombre ingresado no existe.\n")
        
"""
En esta funcion salir, se importo la libreria time para poner un timeout de 2 segundos al cerrar la aplicacion!
"""
def salir():
    opc = 5
    print("Cerrando la agenda..")
    time.sleep(2)
    return opc

def menu():
    opc = 6
    while 1 >= opc or opc >= 5:
        opc = int(input("Ingrese una opcion:\n1- Consultar\n2- Añadir\n3- Modificar\n4- Borrar\n5- Salir\n"))
        if opc == 1:
            consultar()
            opc = 9
        elif opc == 2:
            añadir()
            opc = 9
        elif opc == 3:
            modificar()
            opc = 9
        elif opc == 4:
            borrar()
            opc = 9
        elif opc == 5:
            opc = salir()
menu()