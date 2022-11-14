"""
Pedir dos números y mostrar la tabla de multiplicar del primer número.
El segundo número indicara hasta donde se debe llegar al mostrar la tabla.
Por ejemplo, para los numero 4 y 15 se mostrará la tabla de multiplicar del numero 4, 
comenzando en 4 x 1, y llegando hasta 4 x 15. Validar que los números sean mayores a cero.

def tablaMultiplicar(numero1,numero2):
    for i in range(1,numero2+1):
        print(str(numero1),"x",str(i))
        #print(numero1,"x",i)

tablaMultiplicar(4,15)

"""






"""
Para calcular el vuelto de una compra, pedir dos cantidades, donde la primera cantidad es el monto que se cobra y 
la segunda es lo que entrega quien compra. Según esos dos valores mostrar el vuelto a entregar e indicar la distribución 
del vuelto que se entrega. Por ejemplo, para los valores 45 y 100, el vuelto será de 65 (se cobra 45 y la persona da un billete de 100), 
y este vuelto estará distribuido en 1 billete de 50, un billete de 10, y un billete de 5 (50 + 10 + 5 = 65).


vuelto=dinero-precio

375=3*100+1*50+2*10+1*5
385=3*100+1*50+3*10+1*5
"""


def vuelto(cantidad1,cantidad2):
    vuelto=cantidad2-cantidad1
    billete1=int(vuelto/100)
    billete2=int((vuelto-billete1*100)/50)
    billete3=int((vuelto-billete1*100-billete2*50)/10)
    billete4=int((vuelto-billete1*100-billete2*50-billete3*10)/5)
    print(billete1)
    print(billete2)
    print(billete3)
    print(billete4)


vuelto(15,400)



