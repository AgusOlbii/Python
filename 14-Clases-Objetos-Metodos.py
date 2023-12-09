"""
Programacion orientada a objetos:
Es un paradigma de programacion que permite usar objetos para diseñar aplicaciones
y programas de computadora. Es ampliamente utilizado porque el codigo escrito
es organizado, reutilizable y facil de mantener. 
Los beneficios de este paradigma incluyen:
-La reutilizacion
-La escalabilidad
-La eficiencia del codigo

Las Clases:
Son plantillas que contienen metodos y atributos, estas sirven para crear
los obetos. Por otro lado, los objetos son una instancia de la clase.
EJEMPLO:
CLASE: ANIMAL
    |
    v
ATRIBUTOS: 
        - Nombre
        - Edad
        - Peso
    |
    v
METODOS: 
        - Caminar
        - Comer
        - Dormir
OBJETOS:
        - Gato
        - Perro
        - Lobo
"""
class Bicicleta: #Self no es una palabra reservada, lo que quiere decir que en su lugar podemos usar otra palabra
    #Este es un metodo constructor
    def __init__(self, color, cambios, rin): #El init inicializa los atributos de esta clase
        self.color = color,
        self.cambios = cambios,
        self.rin = rin
    #Estos son metodos de la clase Bicicleta
    def frenar(self):
        return "La bicicleta esta frenando."
    def avanzar(self):
        return "La bicicleta esta avanzando. "
    def girar(self):
        return "La bicicleta esta girando."
#Creacion de objetos:
urbana = Bicicleta("Rojo", 8, 27.5)

hibrida = Bicicleta("Azul", 1, 29)

print(f"Urbana: {str(urbana.color)}")

print(f"Urbana: {urbana.girar()}")