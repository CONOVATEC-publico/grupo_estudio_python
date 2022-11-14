"""
Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla.



asignaturas = ["Matemáticas", "Física", "Química", "Historia","Lengua"]

print(asignaturas)
"""




"""

Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.


def listar(listaAsignaturas):
    for i in range(0,len(listaAsignaturas)):
        print("Yo estudio "+listaAsignaturas[i])



def listar(listaAsignaturas):
    for i in listaAsignaturas:
        print("Yo estudio "+i)

asignaturas = ["Matemáticas", "Física", "Química", "Historia","Lengua"]

listar(asignaturas)

"""




"""
Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante.



abecedario = ["a", "b", "c", "d","e","f", "g", "h", "i","j","k", "l", "m", "n","o","p", "q", "r", "s","t","u", "v", "w", "x","y","z"]
print(abecedario)

def quitarMultiplos(abc):
    for i in range(len(abc),1,-1):
        if(i%3==0):
            indice=i-1
            print("i",i)
            abc.remove(abecedario[indice])
    print(abc)

quitarMultiplos(abecedario)

"""




"""


Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

adrian

"""


vocales=["a","e","i","o","u"]

#palabra="adrian"
#print(palabra.find("a"))
#print(palabra.rfind("a"))
#print(palabra.count("a"))



palabra=input("Ingrese una palabra: ")

def contarVocales(texto):
    for i in vocales:
        print("cantidad de "+str(i)+": ",texto.count(i))


contarVocales(palabra)


