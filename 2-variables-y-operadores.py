"""
Variables: Almacena informacion que pude cambiar durante
la ejecucion del programa.
-No es necesario declarar el tipo de variable
-Es de tipado dinamico. Se encarga de reconocer y trabajar
con los valores almacenados. Es posible cambiar el tipo
de dato
durante la ejecucion. Enteros, Flotantes, Cadenas, Booleano
"""

nombre = "Agustin Olbinsky"
numero = 3412006055
estatura = 1.80
print("Hola " + nombre + ", Bienvenido al mundo de python.")
 

print("Hola! " + nombre + ", tu numero es: "+ str(numero))

print(f"hola! {nombre}, tu numero es: {numero}")

print (f"Hola!, {nombre}, tu numero de telefono es: {numero} y tu altura es: {estatura}")



#Operadores: Permiten manipular las variables para todo.
"""
    Los operadores son simbolos que indican como se deben
manipular los operadores.
    Los operadores junto a los operandos forman una expresion, que es una formula que define el calculo de un valor.
    
    Distintos tipos de operadores:
    -Operadores aritmeticos.
        -Suma: +
        -Resta: -
        -Multiplicacion * 
        -Division: /
        -Modulo: %
    -Operadores Logicos.
        -And: y -> Devuelve true si solo si true + true
        -Or: o -> Devuelve true si solo si alguno de los dos es true: true + false, false + true , true + true
        -Not: no -> Devuelve el opuesto.
    -Operadores relacionales. 
        - == -> Son iguales?
        - != -> Son Distintos?
        - >  -> Es a mayor que b
        - >= -> Es a mayor o igual que b
        - <  -> Es a menor que b
        - <= -> Es a menor o igual que b
    -Operadores de asignacion. 
        - +=
        - -=
        - /=
        - %= 
"""
#ACTIVIDAD 1 OPERACIONES: 
"""
    El día de hoy, tienes el reto de implementar un programa muy sencillo basado en la línea de comandos. Su programa deberá aceptar las entradas de esta manera:
    Ingresa el primer número: 3
    Ingresar el segundo número: 4
    Después, con los números ingresados (3 y 4) deberá mostrar los siguientes resultados:

            3 + 4 = 7
            3 * 4 = 12
            3 == 4 : false
            3 < 4 : true
            4 >= 3 : true 
"""
numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")
print(f"""
        {numero1} + {numero2} = {int(numero1) + int(numero2)}
        {numero1} * {numero2} = {int(numero1) * int(numero2)}
        {numero1} == {numero2} = {int(numero1) == int(numero2)}
        {numero1} < {numero2} = {int(numero1) < int(numero2)}
        {numero2} >= {numero1} = {int(numero2) >= int(numero1)}
        """)