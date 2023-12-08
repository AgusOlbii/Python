"""
    -IF     --> SI
    -ELSE   --> SI NO
    -ELIF   --> SI NO, NO

"""
condicion = True
#Estructura IF: 
if condicion:
  pass
else:
    pass

#Estructura IF ANIDADO
if condicion:
    pass
elif condicion:
    pass
else:
    pass

""" EJEMPLO 1
    Crear un programa que reciba el numero de años que tiene nuestra computadora
    Imprimir en consola si es nueva o vieja.
    Condiciones: Si es menor o igual a 2 años, entonces es nueva. 
    Pero, si es mayor a dos años, entonces es vieja. 
"""
edad = int(input("Cuantos años tiene tu computadora?: "))
if edad <= 2:
    print("Su comutadora es nueva.")
else:
    print("Su computadora es vieja.")
    
""" EJEMPLO 2
    Crea un programa para ingreso a un boliche, si la persona es mayor de 21 pasa al vip,
    si la persona es menor de 21 pero mayor o igual que 18 va al general, si la persona tiene
    menos de 18 no entra. 
"""
edad_persona = int(input("Ingrese la edad de la persona: "))
if edad_persona < 18:
    print("No puede ingresar por ser menor de edad.")
elif edad_persona < 21:
    print("Ingrese al gral")
else:
    print("Ingrese al vip")
    
#IF ANIDADO
persona = int(input("Cuantos años tiene? "))
graduacion = input("Ya te has graduado? (si) o (no)")

if persona > 18:
    print(" Felicidades! Ya sos mayor de edad.")
    if graduacion == "si" or graduacion == "SI":
        print("Felicidades! ya te has graduado")


password = input("Ingrese su nueva contraseña: ")
if len(password) < 8:
    print("La contraseña que desea ingresar es demasiado corta. Intente con una mas larga.")
elif len(password) > 8:
    print("La contraseña que ha ingresado es valida! Ingrese su nueva contraseña para iniciar sesion: ")
    password1 = input("")
    if password != password1:
        print("La contraseña ingresada es invalida, intentelo nuevamente")
    else:
        print("Ha ingresado con exito!")
        
""" ACTIVIDAD 2
    Descripción del problema
Imagine que la tienda donde usted trabaja ofrece descuentos a los clientes en navidad, de acuerdo con el monto de su compra.
El criterio para establecer el descuento se muestra a continuación:
Compra (USD)
Porcentaje
Sí es menor a 80
0%
Sí es mayor o igual a 80 y menor que 150
10%
Sí es mayor o igual a 150 y menor o igual a 300 
15%
Sí es mayor a 300 y menor a 500 
20%
Teniendo en cuenta la tabla, te piden que escribas un programa que solicite el nombre del cliente y el valor de la compra. Y que arroje como resultado: 
Recuerde que para calcular el descuento primero debe multiplicar el valor de la compra por el porcentaje. Luego, debe restar el valor obtenido al valor
de la compra y con eso obtiene el precio con descuento.
descuento = valor_compra x porcentaje
precio final = valor_compra - descuento
"""
cliente = input("Ingrese el nombre del cliente: ")
venta = input("Ingrese el valor de la venta sin descuentos: ")

if int(venta) < 80:
    print(f"""
          {cliente}
          ${venta}
          ${venta} No se aplican descuentos.
            """)
elif int(venta) >= 80 and int(venta) < 150:
        print(f"""
                {cliente}
                ${venta}
                ${int(venta) - (int(venta) * 10 /100)} Precio con el 10% de descuento aplicado
              """) 
elif int(venta) >= 150 and int(venta) <= 300:
            print(f"""
                {cliente}
                ${venta}
                ${int(venta) - (int(venta) * 15 /100)} Precio con el 15% de descuento aplicado
              """) 
elif int(venta) > 300 and int(venta) < 500:
            print(f"""
                {cliente}
                ${venta}
                ${int(venta) - (int(venta) * 20 /100)} Precio con el 20% de descuento aplicado
              """)
else:
    print("Usted ha gastado tanto que no tenemos forma de agradecerle. chauchis")