"""
Descripción del problema
Los asesores en los bancos se enfrentan a una pregunta común de parte de los ciudadanos:
¿Debo pagar impuestos por tener dinero en el banco? Muy bien, el día de hoy vamos a escribir
un programa para dar respuesta a esta inquietud.

 

Implementa un programa con una clase llamada Persona que contenga dos atributos que serán
ingresados por teclado: nombre y edad. Además, que contenga un método llamado imprimir que
devuelva el nombre y la edad.

 

Después, crea otra clase llamada Ciudadano que herede de la clase Persona y agregue un atributo
llamado depósito que será ingresado por teclado. Además, contendrá el método llamado imprimir
para mostrar el depósito. 

 

Así mismo, crea otro método llamado impuestos y si el depósito es superior a 4000 USD muestre que
SI debe pagar, caso contrario no deberá pagar. 

 

Los datos para este ejercicio son los siguientes:

 

Nombre              Edad        Depósito

Manuel Chima        25            6700

Fayle García        56            3500

Lesly Rodríguez     34            9000

Mario Herrera       45            2500
"""

"""
Implementa un programa con una clase llamada Persona que contenga dos atributos que serán
ingresados por teclado: nombre y edad. Además, que contenga un método llamado imprimir que
devuelva el nombre y la edad.
"""
class Persona():
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    def imprimir(self):
        print(f"Nombre: {self.nombre}\n Edad: {self.edad}\n")
        
"""
Después, crea otra clase llamada Ciudadano que herede de la clase Persona y agregue un atributo
llamado depósito que será ingresado por teclado. Además, contendrá el método llamado imprimir
para mostrar el depósito.
Así mismo, crea otro método llamado impuestos y si el depósito es superior a 4000 USD muestre que
SI debe pagar, caso contrario no deberá pagar. 
"""
class Ciudadano(Persona):
    def __init__(self):
        super().__init__()
        self.deposito = int(input(f"Ingrese el deposito de {self.nombre}: "))
        super().imprimir()
        print(f"Nombre: {self.nombre}\n Edad: {self.edad}\n Deposito: {self.deposito}\n")
    
    def impuestos(self):
        if self.deposito > 4000:
            print(f"Si, {self.nombre} debe pargar impuestos\n")
        else:
            print(f"No, {self.nombre} debe pagar impuestos\n")
            
#ciudadano1 = Ciudadano()
#ciudadano1.imprimir()
#ciudadano1.impuestos()

clientes = {
    "cliente1": {"Nombre": "Manuel Chima", "Edad: ": 25, "Deposito": 6700},
    "cliente2": {"Nombre": "Fayle Garcia", "Edad: ": 56, "Deposito": 3500},
    "cliente3": {"Nombre": "Lesly Rodriguez", "Edad: ": 34, "Deposito": 9000},
    "cliente4": {"Nombre": "Mario Herrera", "Edad: ": 45, "Deposito": 2500}
}

def menu():
    opc = True
    while opc == True:
        opc = int(input("Ingrese una opción:\n 1-Ingresar nuevo cliente.\n 2-Eliminar Cliente.\n 3-Mostrar Clientes\n 4-Informe Impuestos\n"))
        if opc == 1:
            nuevo_cliente()
            opc = True
        elif opc == 2:
            eliminar_cliente()
            opc = True
        elif opc == 3:
            mostrar_clientes()
            opc = True
        elif opc == 4:
            informe_impuestos()
            opc = True
            pass
        elif opc == 5:
            opc = False
        
        
def nuevo_cliente():
    cliente = Ciudadano()
    clientes[f"cliente{len(clientes) + 1}"] = {
        "Nombre: ": cliente.nombre,
        "Edad: ": cliente.edad,
        "Deposito: ": cliente.deposito
    }
    
def eliminar_cliente():
    nombre = str(input("Ingrese el nombre del cliente que desea eliminar: \n"))
    
    for i in range(len(clientes)):
        if nombre in clientes.values(nombre):
            del(clientes[i])
            print(f"El cliente {nombre} ha sido eliminado.")
        else:
            print(clientes.keys())
            print("\n\n\n")
            print(clientes.values())
            print(f"El cliente {nombre} no existe.")
            break
        
def mostrar_clientes():
    print("Lista de clientes:\n")
    print(clientes)
    
def informe_impuestos():
    pass
        
menu()