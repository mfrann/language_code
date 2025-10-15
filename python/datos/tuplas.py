
#TUPLAS

'''
No permite cambiar datos almacenados

count -> contar elementos
index -> devolver indice

No usa remove
'''

#EJEMPLOS

numbers = (5,6,7,12,12,13,45,67,67,8,8)

number = int(input("Dame un numero: "))
#print(f'El numero se repite ' + str(numbers.count(number)) + " veces")

print("El numero " + str(number) + "se encuentra en el indice " + str(numbers.index(number)))



