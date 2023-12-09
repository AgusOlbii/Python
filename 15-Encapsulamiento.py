"""
El encapsulamiento hace referencia a la capacidad que tiene un objeto de ocultar su estado,
de manera que sus datos solo se puedan modificar por los metodos accesores. 
Por defecto todos los metodos y atributos de una clase son publicos,
es decir que se puede acceder a los atributos y metodos de dicha clase. 
Existe una forma de indicarle al programa que un dato sera privado.
"""

"""
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._proyecto = proyecto #Con un _ antes de definirla nos indica que podemos acceder a ella desde la clase y sus subclases.
        self.__salario = salario #Con dos _ antes de definirla nos indica que podemos acceder a ella desde la clase. 
"""

class Persona():
    def __init__(self, identificacion, nombre, edad):
        self.__identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
    def saludo(self):
        return "Hola " + self.nombre
    
    """Para poder ver un atributo privado lo podemos hacer atraves de este metodo"""
    def getIdentidicacion(self):
        return self.__identificacion

    def setIdentificacion(self, valor):
        self.__identificacion = valor

persona1 = Persona(45343, "Agus", 15)

print("Vemos el atributo con esta sintaxis " + str(persona1._Persona__identificacion)) #Con esta sintaxis se puede acceder al atributo privado. 
print("Vemos el atributo con el get: " + str(persona1.getIdentidicacion))
print(persona1.nombre)
print(persona1.edad)

"""Con el metodo set podremos cambiar el valor de el atributo privado"""
persona1.setIdentificacion(12345)
print(persona1.getIdentidicacion())