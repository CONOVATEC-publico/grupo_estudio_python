"""
https://aprendeconalf.es/docencia/python/ejercicios/funciones/

Ejercicio 9
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.


12,18

6

20%50

"""

from audioop import reverse


a=12
b=18

def mcd(numero1,numero2):
    mcd=0
    menor=0
    if(numero1<numero2):
        menor=numero1
    else:
        menor=numero2

    for i in range(1,menor):
        if numero1%i==0 and numero2%i==0:
            mcd=i

    return  mcd


print("El mcd de", str(a) ," y ", str(b), " es: ",mcd(a,b))

def mcm(numero1, numero2):
    mcm=0
    mcm=(numero1*numero2)/mcd(numero1,numero2)

    return mcm

print("El mcm de", str(a) ," y ", str(b), " es: ",mcm(a,b))


"""
Ejercicio 10
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.


"""


def decimal_a_binario(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        # se almacena el módulo en el orden correcto
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario

print("metodo 1: ",str(decimal_a_binario(15)))



def decimalAbinario(numero):
    resultado=""
    numero_decimal = numero
    while numero_decimal != 0:
        modulo = numero_decimal % 2
        cociente = numero_decimal // 2
        resultado = str(modulo) + resultado
        numero_decimal = cociente
    print("metodo 2: ",resultado)

decimalAbinario(15)


def nToDecimal(numero,base):
    resultado=0
    for i in range((len(str(numero))-1),-1, -1):
        exponente=(len(str(numero))-1)-i
        resultado+=int(str(numero)[i])*pow(base,exponente)

    return resultado

print("numero decimal es:",nToDecimal(333,4))


"""
a="123"
aRevertido=a[len(a)-1: : -1]
print(aRevertido)

"""

1*1+1*2+1*4+1*8




