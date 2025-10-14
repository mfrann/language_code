#CICLO FOR

'''
i: variable con cualquier otro nombre

in: palabra reservada, siempre se coloca

elemento: el que se va a iterar, lista, 
secuencia de numeros, etc


for i in elemento:
    instruccion
    print()
'''

#EJEMPLO
'''
word = input("Ingresa una palabra: ")

for i in range(10):
    print(word)

'''

#EJEMPLO 2
'''
array = [0, 2, 3, 5, 7]

for i in array:
    print(f' i vale {i} y su cuadrado es {i ** 2}')

print("fINAL")

'''
num = int(input("Numero: "))

print(f'Tabla de multiplicar del {num}')

for i in range(1, 1000):
    print(f'{i} x {num} = {i*num}')
