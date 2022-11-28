
from diccionarios import diccionario2_dia
from diccionarios import diccionario_dia
from diccionarios import listaDiccionario_meses_dias
from diccionarios import dia0


def calcularDia(numero_dias,dia_0):
    resto=numero_dias%7#resto=2
    temp=diccionario2_dia[dia_0]
    temp+=resto
    print("temp::",temp)
    resto2=temp%7
    resultado=diccionario_dia[resto2]
    return resultado

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

cantidad_Dias=cantidadDias(13,"Noviembre")
print ("cantidad:::",cantidad_Dias)
print("dia:::",calcularDia(cantidad_Dias,dia0))


def determinarFecha(fecha):
    print("type:",type(fecha))
    #fecha_string = str(fecha)
    print("fecha:",fecha)
    separador = "/"
    cadena = fecha.split(separador)
    lista_cadena = list(cadena)
    print("lista:",lista_cadena)
    mes=determinarMes(fecha)
    cantidad_Dias=cantidadDias(int(lista_cadena[0]),mes)
    dia_str = calcularDia(cantidad_Dias,"Viernes")

    print(dia_str,",",lista_cadena[0]," de ",mes)




def determinarMes(fecha):

    return "Noviembre"

