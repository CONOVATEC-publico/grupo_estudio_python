"""""

Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


edad=input("Ingresar edad: ")

if int(edad)>17:
    print("Mayor de edad")
else:
    print("Menor de edad")



"""


"""
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
 pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el 
 usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


contraseña="SysTem7255"

contraseñaNueva=input("Ingrese contraseña: ")

if contraseña.upper() == contraseñaNueva.upper():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")



"""


edad=input("Ingresar edad: ")

if int(edad)<17:
    print("Menor de edad")
elif int(edad)>17 and int(edad)<60:
    print("Mayor de edad")
else:
    print("3era edad")
