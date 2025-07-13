import random 

#PROGRAMA PARA SUMAR 

'''
a = int(input("Your first number: "))
b = int(input("Your second number: "))

sum = a + b
sus = a - b 

print("The sum is: ", suma)
print("The sus is: ", resta)

'''

#PROGRAMA TABLA DE MULTIPLICAR
'''
n = int(input("Write your number: "))

print("Tabla de multiplicacion de", n )

for i in range(1,11):
    result = n * i 
    print(n, " x ", i, "=", result)

'''

#PREGUNTAR SI UN NUMERO ES PRIMO O NO
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Tell me your number: "))

if is_prime(n):
    print(n, "Is prime")
else:
    print(n, "Not prime ")
'''

#ADIVINA EL NUMERO 

secret_num = random.randint(1,20)

print("Welcome a The Secret Number :3")
print("You have to guess the secret number, can you? :) ")

n = 0

while True:
    num = int(input("=> "))
    n += 1

    
    if num < secret_num:
        print("Tu numero es menor que el secreto")
    elif num > secret_num:
        print("Tu numero es mayor que el secreto")
    else:
        print("You win!! in ", n, "attempts. :3" )
        break