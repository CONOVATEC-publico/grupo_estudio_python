"""
Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha 
cumplido (desde 1 hasta su edad).

edad=input("Ingresar edad: ")

for i in range(1,int(edad)+1):
    print(i)


Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
los números impares desde 1 hasta ese número separados por comas.

"""

cantidad=input("Ingresar cantidad: ")
numerosImpresos=""
for i in range(1,int(cantidad)+1):
    if i%2!=0:
        numerosImpresos=numerosImpresos+str(i)+","

print(numerosImpresos)

##pop




