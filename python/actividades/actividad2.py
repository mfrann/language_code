

'''
Caso
Imagina que la tienda donde usted trabaja 
ofrece descuentos a los clientes en navidad, 
de acuerdo con el monto de su compra. 
El criterio para establecer el descuento se 
muestra a continuación:

'''


#SOLICITAR INFORMACION

name = input("Tu nombre: ")
value = int(input("El valor de tu compra: "))
porcentaje = [0, 0.1, 0.15, 0.2]

print("BOLETA")
print('Nombre: ' + name)
print('Valor: ' + str(value))

if value < 80:
    descuento = value * porcentaje[0]
    precio_final = value - descuento
    print(f'Precio final es {precio_final}')

elif value >= 80 and value < 150:
    descuento = value * porcentaje[1]
    precio_final = value - descuento
    print(f'Precio final es {precio_final}')

elif value >= 150 and value < 300:
    descuento = value * porcentaje[2]
    precio_final = value - descuento
    print(f'Precio final es {precio_final}')

elif value > 300 and value < 500:
    descuento = value * porcentaje[3]
    precio_final = value - descuento
    print(f'Precio final es {precio_final}')
else: 
    print("Lo sentimos, algo ha fallado")



'''
Ahora responde el interrogante en un 
comentario multilínea ¿Cuál es el 
valor de las siguientes compras con descuento?

Angel Mario Villa Lopez: 455 usd.  --> pf: 364 usd
Rosa Diaz: 105 usd.                --> pf: 94.5 usd
Dilan Gonzalez: 250 usd.           --> pf: 212.5 usd
Kelly Daza: 430 usd.               --> pf: 344 usd

'''