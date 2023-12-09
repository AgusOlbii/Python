"""
La herencia es la capacidad de reutilizar una clase extendiendo su funcionalidad.
Clase PADRE: ATRIBUTOS, METODOS
    |
    V
Clase HIJA: ATRIBUTOS, METODOS. 

"""
class Vehiculo():
    def __init__(self, matricula, modelo, marca, color):
        self.matricula = matricula
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.avanza = False
        self.frena = False
        self.gira = False
        
    def avanzar(self):
        self.avanza = True
    
    def frenar(self):
        self.frena = True
        
    def girar(self):
        self.gira = True
    
    def imprimir(self):
        print(f"""Matricula: {self.matricula} \n Modelo: {self.modelo} \n Marca: {self.marca} \n Color: {self.color}
               \n Avanzar: {self.avanza} \n Frenar: {self.frena} \n Girar: {self.gira}
               """)
        
        
class Moto(Vehiculo):
    def __init__(self, matricula, modelo, marca, color, cilindrada):
        #CON SUPER LE PODREMOS ASIGNAR UN NUEVO ATRIBUTO A LA CLASE HIJA
        super().__init__(matricula, modelo, marca, color)
        self.cilindrada = cilindrada

moto1 = Moto("A021", "XR250", "Honda", "Rojo", 250)
print("------------------")
moto1.avanzar()
moto1.imprimir()
print(moto1.cilindrada)