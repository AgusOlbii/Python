"""
Diccionarios: Los diccionarios son una coleccion de elementos, donde cada uno
tiene una llave y un valor. 

Los diccionarios tienen metodos para insertar, limpiar, eliminar, devolver llaves y devolver
valores en forma de lista. 

"""







"""
#Primera forma de crear un diccionario:

nombre_diccionario = {
    "key": "Value",
    "llave": "valor",
    "Nombre": "Agustin"
    }
print(nombre_diccionario)


#Segunda forma de crear un diccionario:

nombre_diccionario2 = dict(Nombre="Agustin", Edad = "18")
print(nombre_diccionario2)

#Tercera forma de crear un diccionario:

nombre_diccionario3 = dict({
    ("Nombre", "Agustin"),
    ("Edad", 22),
    ("Documento", 4839409)
})
print(nombre_diccionario3)

"""
inventario = {
    "manzana": 235,
    "peras": 400,
    "naranjas": 250,
    "sandias": 500
}
#Devuelve la llave
print("LLaves: \n")
print(inventario.keys())
print("-----------------")
#Devuelve el valor
print("Valores: \n")
print(inventario.values())
print("-----------------")
#Devuelve en forma de lista
print("En forma de lista: \n")
print(inventario.items())