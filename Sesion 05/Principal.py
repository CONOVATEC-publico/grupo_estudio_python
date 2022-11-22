from diccionarios import cantidadDias
from diccionarios import calcularDia
from diccionarios import determinarMes

def determinarFecha(fecha):
    fecha_string = str(fecha)
    separador = "/"
    cadena = fecha_string.split(separador)
    lista_cadena = list(cadena)
    dia_str = calcularDia(lista_cadena[0],"Viernes")
    return print(dia_str,",",lista_cadena[0])
    #return "Domingo, 30 de octubre de 2022"

determinarFecha(21/11/2022)