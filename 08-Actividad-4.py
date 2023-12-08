"""
Descripción del problema
¿Se acercan tus próximas vacaciones en el extranjero y aún no has definido tu presupuesto? Muy bien, un conversor
de monedas puede ser muy útil en estos casos, porque te permitirá conocer el valor de tu moneda en otro país
y de esta manera puedes prepararte para pasear y comprar el producto que más te guste. ¡Genial!
Escribamos un programa que permita calcular el valor de dolares o euros a:
pesos colombianos, yuanes, libras esterlinas. 
En esta actividad usaremos un valor promedio para determinar la equivalencia, mire las siguientes tablas:

Dólar (USD)     Equivale a      Moneda 

    1               3750      pesos colombianos

    1               6.37        yuanes

    1               0.76      libras esterlinas

Euro (€)        Equivale a      Moneda 

    1               4000       pesos colombianos

    1               6.93        yuanes

    1               0.83     libras esterlinas
La función principal tendrá como parámetros: 
-El nombre de la moneda actual. 
-El valor de la moneda actual. 
-Y el nombre de la moneda a convertir. 

Y dentro de la función principal estarán dos subfunciones dolarTo() y euroTo(), las cuales se encargarán de
ejecutar las condiciones que permitirán obtener el valor equivalente a la moneda actual.


Nota: Para obtener la equivalencia de una moneda u otra solo basta multiplicar:
moneda actual x equivalente. Por ejemplo, si un dólar es igual a 6.37 yuanes.
¿A cuánto equivale 8 dólares? Simplemente, multiplicamos: 8 x 6.37 = 50.94 yuanes.
"""

def func_principal(nombre_actual, valor_actual, nombre_convertir):
    conv_a_dolar = 0
    conv_a_euro = 0
    if nombre_convertir == "dolares":
        def dolarTo(nombre_actual, valor_actual):
            if nombre_actual == "pesos colombianos":
                return valor_actual * 3750
            elif nombre_actual == "yuanes":
                return valor_actual * 6.37
            elif nombre_actual == "libras esterlinas":
                return valor_actual * 0.76
        conv_a_dolar = dolarTo(nombre_actual, valor_actual)
        print(f"{valor_actual} dolares equivale a {conv_a_dolar} {nombre_actual}")
    elif nombre_convertir == "euros":
        def euroTo(nombre_actual, valor_actual):
            if nombre_actual == "pesos colombianos":
                return valor_actual * 4000
            elif nombre_actual == "yuanes":
                return valor_actual * 6.93
            elif nombre_actual == "libras esterlinas":
                return valor_actual * 0.83
        conv_a_euro = euroTo(nombre_actual, valor_actual)
        print(f"{valor_actual} euros equivale a {conv_a_euro} {nombre_actual}")

def menu():
    salir = 1
    while salir == 1:
        moneda_a_convertir = str(input("Ingrese a que moneda desea convertir (euros o dolares): "))
        moneda_actual = str(input("Ingrese que moneda desea convertir (yuanes, pesos colombianos o libras esterlinas): "))
        valor = float(input(f"Ingrese la cantidad de {moneda_a_convertir} que desea convertir a {moneda_actual}: "))
        print("Realizando calculos..")
        func_principal(moneda_actual, valor, moneda_a_convertir)
        salir = int(input("0.Salir | 1.Realizar otro cambio de monedas"))
        if salir == 0:
            print("Gracias por utilizar este conversor de monedas! Hasta luego.")
menu()
        
        
