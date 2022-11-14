diccionario_dia={
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
"""
31 dic 2021 viernes

01 enero
08 enero
09 enero

sabado,domingo,lunes,martes,miercoles

"""

resto=26%7
#5
temp=diccionario2_dia['Viernes']
temp=temp+resto#10
resto2=temp%7#3
resultado=diccionario_dia[resto2]

print("dia::",resultado)


print(sum(diccionario2_dia.values()))


