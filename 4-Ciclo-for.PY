"""
I   -> Es una variable que puede tener cualquier otro nombre. 
IN  -> Es una palabra reservada, es decir, siempre se debe colocar y no
        podremos asignarle ese nombre a una variable. 
Elemento    -> Es el que va a iterar, puede ser una lista, una secuencia de numeros, etc. 

"""
#Primer ejemplo
word = input("Ingrese una palabra: ") #-> Creamos una entrada de datos
for i in range(10): #-> Le decimos a la maquina que itere lo que haya dentro del for 10 veces
    print(word, i+1)
 
#Segundo Ejemplo:
contador = 1
print("Comienzo")
for i in [3, 4, 5]:
    print(f"Vuelta numero: {contador}")
    print(f"Hola!, ahora i vale {i} y su cuadrado es {i ** 2}")
    contador += 1
print("Final") 

#Tercer Ejemplo:
numero = int(input("Ingrese un numero asi se le mostrara la tabla del 1 al 10: "))
print(f"Tabla de multiplicar de {numero}")
for i  in range(10):
    print(f"{i + 1} x {numero} = {(i + 1) * numero}") #ATENCION! A I SE LE SUMA 1 CADA QUE ITERA, POR ESO EN EL RANGE SE PONE 10, SINO SERIA 11.
