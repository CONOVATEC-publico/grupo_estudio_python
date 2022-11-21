from diccionarios import cantidadDias
from diccionarios import determinarMes

def determinarFecha(fecha):
    fecha_string = str(fecha)
    separador = "/"
    cadena = fecha_string.split(separador)
    lista_cadena = list(cadena)
    return print(lista_cadena)
    #return "Domingo, 30 de octubre de 2022"
determinarFecha(30/10/2022)