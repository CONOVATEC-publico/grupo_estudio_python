"""""
Ejercicio 1

Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombreUsuario=input("Escribir nombre: ")
numeroRepeticion=input("Escribir numero de repeticiones: ")

print(type(nombreUsuario))
print(type(numeroRepeticion))

for n in range(int(numeroRepeticion)):
    print(nombreUsuario)


Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con 
todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

"""
nombre1="adrian"
numero1=1
numero2=5

suma=numero1+numero2

#print(suma)

#print("adrian")
#print(nombre1)
#print(type(nombre1))

nombreUsuario=input("Escribir nombre: ")

nombre=nombreUsuario.split()[0]
apellido=nombreUsuario.split()[1]

print(nombreUsuario.lower())
print(nombreUsuario.upper())
print(nombre.capitalize(),apellido.capitalize())

#print(nombreUsuario)



