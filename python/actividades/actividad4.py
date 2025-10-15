

'''
Escribamos un programa que permita calcular 
el valor de dólares o euros a: 

Pesos colombianos

Yuanes  

Libras esterlinas. 

1 dolar = 3750 pesos
        = 6.37 yuanes
        = 0.76 libras

        
La función principal tendrá como parámetros:

El nombre de la moneda actual

El valor de la moneda actual

Y el nombre de la moneda a convertir.

'''



print("Bienvenido al conversor de monedas")

moneda_actual = int(input("Cual es tu moneda actual: \n 1. Dolar \n 2. Euro \n >>> "))
valor = float(input("Ingrese la cantidad \n >>> "))
moneda_convertir = input("Elige a que moneda convertir: \n 1. Pesos colombianos \n 2. Yuanes \n 3. Libras \n >>> ")


def conversor(moneda_actual, valor, moneda_convertir):
    if moneda_actual == 1:
        def toDolar():
            if moneda_convertir == "1":
                print(f'{valor} dolares equivale a {valor * 3750} pesos colombianos')
            elif moneda_convertir == "2":
                print(f'{valor} dolares equivale a {valor * 6.37} yuanes')
            elif moneda_convertir == "3":
                print(f'{valor} dolares equivale a {valor * 0.76} libras esterlinas')
            else:
                print("No se reconoce la moneda")
        toDolar()

    elif moneda_actual == 2:
        def toEuro():
            if moneda_convertir == "1":
                print(f'{valor} dolares equivale a {valor * 400} pesos colombianos')
            elif moneda_convertir == "2":
                print(f'{valor} dolares equivale a {valor * 6.93} yuanes')
            elif moneda_convertir == "3":
                print(f'{valor} dolares equivale a {valor * 0.83} libras esterlinas')
            else:
                print("No se reconoce la moneda")
        toEuro()
    
    else:
        print("No se reconoce la moneda")

conversor(moneda_actual, valor, moneda_convertir)



'''

50 usd -> 187500.0 pesos colombianos
30 euros -> 207.89999999999998 yuanes
15 euros -> 12.45 libras esterlinas


'''