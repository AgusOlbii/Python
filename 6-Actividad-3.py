"""
Descripción del problema:
Imagina que culminaste el 5º semestre de la universidad, en el cual viste las siguientes asignaturas:
Seguridad Informática, Ingeniería Web, Inteligencia Artificial, Programación Móvil y Redes; y las notas fueron las siguientes: 5.0, 4.5, 3.6, 3.9 y 4.3
respectivamente. 

Teniendo claro esto, escribe un programa que solicite tu nombre completo, el nombre de las cinco materias y la calificación de cada una.
Y como resultado devuelve tu nombre y el promedio obtenido en el semestre.
Recuerda que la fórmula para calcular el promedio es: 
Promedio = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5)/Cantidad de notas
"""
salir = 1
cont = 0
while salir == 1:
    alumno = str(input("Ingrese el nombre del alumno: "))
    for i in range(5):
        materia = input("Ingrese el nombre de la materia: ")
        nota = float(input(f"Ingrese la nota en {materia}: "))
        cont += 1
        if i+1 == 1:
            materia1 = materia
            nota1 = nota
        elif i+1 == 2:
            materia2 = materia
            nota2 = nota
        elif i+1 == 3:
            materia3 = materia
            nota3 = nota
        elif i+1 == 4:
            materia4 = materia
            nota4 = nota
        elif i+1 == 5:
            materia5 = materia
            nota5 = nota
    promedio = (nota1 + nota2 + nota3 + nota4 + nota5)/cont
    print(f"El promedio de {alumno} es {round(promedio,2)}!")
    salir = int(input("Si desea salir presione 0, si desea ver el promedio de otro alumno presione 1"))