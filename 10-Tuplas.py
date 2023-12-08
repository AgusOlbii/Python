"""
Guardan los datos separados por comas y su uso es muy similar a las listas,
con la diferencia de que las tuplas son inmutables, t por lo tanto no
permiten modificar los datos almacenados.

La gran ventaja que ofrecen las tuplas es el poco espacio que ocupan en memoria,
dado que al ser inmutables, no necesitan reservar espacio adicional como en el caso de las listas.

Las tuplas cuentan con los siguientes metodos:
count: sirve para contar cuantos elementos tiene la tupla. 
index: sirve para saber en que posicion se encuentra un elemento. 
"""

#Primer Ejemplo:
"""
Crear una tupla con numeros, luego pedir un numero por teclado y luego indicar cuantas veces se repite en la tupla.
"""
numeros = (5, 6, 7, 8, 5, 5, 6, 90, 12, 14, 12)

numero = int(input("Ingrese un numero: "))

print(f"El numero se repite: {str(numeros.count(numero))} y se encuentra en el indice: {str(numeros.index(numero))}")