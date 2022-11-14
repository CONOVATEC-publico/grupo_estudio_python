"""

Escriba un programa que ordene las palabras de una frase en orden descendente de acuerdo al tamaño de las mismas.
Imprima cada palabra con su respectiva longitud.
a) Ingresado el texto, generar una lista de tuplas, cada tupla es de dos items, tamaño de la palabra y la palabra misma.
b) Imprimir la lista de tuplas.
c) Ordenar la lista de tuplas en orden descendente de acuerdo al tamaño de las palabras.
d) Imprimir la lista ordenada.
e) Imprimir cada item de la lista de la siguiente manera: La palabra "yyyy" tiene yy caracteres.


"""

"""
#Hola mundo
frase=input("Ingresa frase: ")



frase_lista = frase.split(" ")

print(frase_lista)
longitud=len(frase_lista)
print(longitud)
lista_tuplas=[]
for i in range(0,longitud):
    tupla_temporal=(len(frase_lista[i]),frase_lista[i])
    lista_tuplas.append(tupla_temporal)

print("lista_tuplas:::",lista_tuplas)

"""

"""
Se define la siguiente lista de tuplas:
lista1 = [('1','2','3','4','5'), ('2','3','4','5','6'), ('3','4','5','6','7'), ('4','5','6','7','8'), ('5','6','7','8','9')]
a) Añadir al final de cada tupla los valores '12345', '23456', '34567', '45678' y '56789' respectivamente y, obtener el siguiente resultado:
lista2 = [('1','2','3','4','5','12345'), ('2','3','4','5','6','23456'), ('3','4','5','6','7','34567'), ('4','5','6','7','8','45678'), ('5','6','7','8','9','56789')]
b) Imprimir la lista de tuplas modificada (lista2) en forma de matriz.

"""

lista1 = [('1','2','3','4','5'), ('2','3','4','5','6'), ('3','4','5','6','7'), ('4','5','6','7','8'), ('5','6','7','8','9')]
lista2=[]
#tupla1=(lista1[0],'12345')
#print("tupla1::",tupla1)

t=('1','2','3','4','5')
print(len(t))

def modificar_tupla(tupla):
    concatenacion=''
    for i in range(0,len(tupla)):
        concatenacion=concatenacion+tupla[i]
        
    tupla_modificada=(tupla,concatenacion)

    return tupla_modificada

print("t -> ",modificar_tupla(t))

def modificarLista(lista):
    lista_modificada=[]
    for i in range(0,len(lista)):
        lista_modificada.append(modificar_tupla(lista[i]))
    
    return lista_modificada

lista2=modificarLista(lista1)

print("lista 2 >>>> ",lista2)




