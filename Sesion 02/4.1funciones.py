a=input("Ingrese valor")
b=input("Ingrese valor")

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


print("El mcd  es: ",mcd(15,40))

def mcm(numero1, numero2):
    mcm=0
    mcm=(numero1*numero2)

    return mcm

print("El mcm de", a ," y ", b, " es: ",mcm(a,b))
