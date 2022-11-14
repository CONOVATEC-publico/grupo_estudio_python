"""
Diccionarios:
1. ¿Cómo se crea un diccionario vacío?

diccionario_vacio={}

print(diccionario_vacio)
print(type(diccionario_vacio))

"""


"""
2. ¿Cuáles de los siguientes diccionarios se encuentran creados correctamente?

d1 = {4 :[2, 3], 7:[5, 6]}
#d2 = {[2, 3]:4, [5, 6]:7}
d3 = {(2, 3):4, (5, 6):7}
d4 = {1:"Perú", 2:"Brasil", 3:"Chile"}
d5 = {"Perú":1, "Brasil":2, "Chile":3}

#d6 = {{2:3}:4, [5, 6]:7}


print("-"*20)
print(d1)
#print(d2)
print(d3)
print(d4)
print(d5)

print("*"*5)
print(d3[(5, 6)])

"""



"""
3.Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre en 
pantalla:
    <nombre del día>, <dd> de <nombre del mes> de <aaaa>

Por ejemplo, si introducimos: 30/10/2022
Se mostrara: Domingo, 30 de octubre de 2022

Utilizar diccionarios para el nombre del día y el nombre del mes.
"""

diccionario_dia={
    0:"Domingo",
    1:"Lunes",
    2:"Martes",
    3:"Miercoles",
    4:"Jueves",
    5:"Viernes",
    6:"Sabado",
    7:"Domingo"
}

diccionario2_dia={
    "Lunes":1,
    "Martes":2,
    "Miercoles":3,
    "Jueves":4,
    "Viernes":5,
    "Sabado":6,
    "Domingo":7
}

listaDiccionario_meses_dias=[
    {
        "mes":"Enero",
        "dias":31
    },
    {
        "mes":"Febrero",
        "dias":28
    },
    {
        "mes":"Marzo",
        "dias":31
    },
    {
        "mes":"Abril",
        "dias":30
    },
    {
        "mes":"Mayo",
        "dias":31
    },
    {
        "mes":"Junio",
        "dias":30
    },
    {
        "mes":"Julio",
        "dias":31
    },
    {
        "mes":"Agosto",
        "dias":31
    },
    {
        "mes":"Septiembre",
        "dias":30
    },
    {
        "mes":"Octubre",
        "dias":31
    },
    {
        "mes":"Noviembre",
        "dias":30
    },
    {
        "mes":"Diciembre",
        "dias":31
    },

]
"""
31 diciembre .->viernes

7 enero viernes
10 enero lunes


10=7+3

365%7
29 enero
"""

dia0="Viernes"

def calcularDia(numero_dias,dia_0):
    resto=numero_dias%7#resto=2
    temp=diccionario2_dia[dia_0]
    temp+=resto
    print("temp::",temp)
    resto2=temp%7
    resultado=diccionario_dia[resto2]
    return resultado

#print("dia:::",calcularDia(29,dia0))

#5 marzo
def cantidadDias(dia,mes):
    total=0
    for i in listaDiccionario_meses_dias:
        #print("messs:",i.get("mes"))
        if i.get("mes")==mes:
            print("breakkk")
            break
        total+=i.get("dias")
    total+=dia
    return total

cantidadDias=cantidadDias(13,"Noviembre")
print ("cantidad:::",cantidadDias)
print("dia:::",calcularDia(cantidadDias,dia0))


def seleccionarDias(fecha):

    return 13


def determinarMes(fecha):

    return "Noviembre"






"""
4.Escribir una función que reciba una cantidad N de iteraciones de una tirada de 2 dados, y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados. Nota: utilizar el módulo random para obtener tiradas aleatorias.
5.Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.
"""






