#FUNCIONES

#LEN: devolver longitud de un elemento
'''
Se usa "def"

def suma(a,b):
    resultado = a+b

print(suma(a,b))


Con parametros

def(param1, param2)
'''

#EJEMPLO
'''
def saludar():
    print("Hola Fran")

saludar()

num1 = int(input("Numero 1: "))
num2 = int(input("Numero2: "))

def suma(a, b):
    print(f'La suma es: {a + b}')

suma(num1, num2)

'''
'''
def esPar(numero):
    if numero % 2 ==0:
        print("Es par")
    else:
        print("Es impar")

esPar(10)
esPar(1)

'''

def multi(num = None):
    if num == None:
        print("Ingresa un numero valido")
    else:
        print(f'TABLA DE MILTIPLICACION DEL {num}')
        for i in range(1,11):
            print(f'{i} x {num} = {i*num}')

numb = int(input("Ingrese un numero: "))
multi(numb)

