"""
El ciclo o bucle while revisa la condicion que es dada; si es verdadera ejecuta las
    instrucciones y luego vuelve a revisar la condicion. 
Este proceso se repite hasta que la condicion sea falsa
"""
#Primer Ejemplo:
contador = 0
while contador != 2:
    contador = int(input("Desea calcular el IMC? 1.SI o 2.NO \n"))
    
    if contador == 1:
        estatura = float(input("Ingrese la estatura en metros: "))
        peso = float(input("Ingrese su peso en kg: "))
        resultado = round(peso/(estatura ** 2), 2) #ATENCION! EL ROUND SIRVE PARA REDONDEAR DECIMALES. AL FINAL DE LA SENTENCIA SE 
                                                   # PONE UNA COMA Y LA CANTIDAD DE DECIMALES QUE QUERRAMOS QUE TENGA
        if resultado < 18.5:
            print(f"IMC {resultado} = Bajo de peso")
        elif 18.5 <= resultado < 24.99:
            print(f"IMC {resultado} = Peso normal")
        elif 25 < resultado < 30:
            print(f"IMC {resultado} = Sobrepeso")
        else:
            print("Usted es obeso")
    elif contador == 2:
        print("Hasta pronto")
print("Gracias por utilizar mi calculadora!")