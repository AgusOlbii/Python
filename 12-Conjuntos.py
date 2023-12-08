"""
Los conjuntos en python son listas donde no existe la repeticion, pero los
elementos no estan ordenados. 
"""
#Primera forma de crear conjuntos
alumnos = {"Biyin", "Mangel", "Rubius", "Auron"}
print(type(alumnos))
print(alumnos)
print("-----------------------------\n")


#Segunda forma de crear conjuntos
lenguajes = set(["PHP", "Python", "JavaScript"])
print(lenguajes)
print("-----------------------------\n")

lenguajes.add("c#")
print(lenguajes)

#lenguajes.clear() Este metodo vacia el conjunto

lenguajes.pop() #Elimina un elemento arbitrario, si el conjunto esta vacio nos ocacionara un error

lenguajes.remove("PHP") #Elimina el elemento que nosotros querramos, si no se encuentra nos dara error

todos = alumnos.union(lenguajes)

print(todos)