"""
Hace refenrencia a que los objetos pueden tomar diferentes formas.
El polimorfismo es un concepto fundamental en la programación orientada a objetos que permite
a objetos de diferentes clases responder a llamadas de métodos de la misma manera.
En otras palabras, el polimorfismo permite que objetos de distintas clases sean tratados de
manera uniforme si implementan métodos con el mismo nombre.
"""
class Gato():
    def sonido(self):
        print("MIAU")
class Perro():
    def sonido(self):
        print("GUAU")
        
        
def escuchar_sonido(animal):
    animal.sonido()
    
gato1 = Gato()

perro1 = Perro()

escuchar_sonido(gato1)

escuchar_sonido(perro1)