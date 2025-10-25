'''
Invertir una cadena
Escribe un programa que tome una cadena ingresada por el usuario y la invierta sin usar funciones integradas como [::-1].
Conceptos practicados: Bucles, manipulación de cadenas, pensamiento iterativo.



cadena = input("Ingresa un texto: \n >>> ")
invertida = ""

for letra in cadena:
    invertida = letra + invertida

print(f'La palabra invertida es: {invertida}')

'''


'''
Suma de dígitos
Escribe un programa que tome un número entero positivo y calcule la suma de sus dígitos. 
Por ejemplo, para 123, la suma es 1 + 2 + 3 = 6.
Conceptos practicados: Bucles, conversión entre tipos, operaciones matemáticas.


num = int(input("Enter a number: \n >>> "))
sum = 0
while num > 0:
    sum += num%10 #agarra el ultimo digito
    num //= 10 #agarra los dos primero digitos

print(f'La suma es {sum}')

'''

'''

Números primos
Escribe un programa que determine si un número ingresado por el 
usuario es primo. Un número primo solo es divisible por 1 y por sí mismo.
Conceptos practicados: Bucles, condicionales, optimización básica.


num = int(input("Enter a number: \n >>> "))
is_Primo = True
if num < 2:
    is_Primo = False

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_Primo = True

print(f'Es primo? {is_Primo}')

'''


'''
Secuencia de Fibonacci
Escribe un programa que genere los primeros n números de la secuencia de Fibonacci, 
donde cada número es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8, ...).
Conceptos practicados: Bucles o recursión, almacenamiento de valores, lógica iterativa.

'''

'''
num = int(input("Ingresa un numero: \n >>> "))
fib = [0,1]

for i in range(2, num):
    fib.append( fib[i-1] + fib[i-2] )

print(f'La secuencia es: {fib[:num]}')

'''

'''
Torres de Hanoi
Resuelve el problema de las Torres de Hanoi para n discos usando recursión. 
El objetivo es mover los discos de una torre a otra siguiendo las reglas clásicas.
Conceptos practicados: Recursión, pensamiento lógico, descomposición de problemas.
'''


def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f'Mover disco 1 de {origen} a {destino}')
        return
    hanoi(n-1, origen, auxiliar, destino)
    print(f'Mover disco {n} de {origen} a {destino}')
    hanoi(n-1, auxiliar, destino, origen)

n = int(input("Ingresa el numero de discos: \n >>> "))
hanoi(n, "A", "B", "C")










