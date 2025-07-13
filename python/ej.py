"Crea una funcion que te de la tabla de multiplicar de un numero n"

n = int(input("Ingresa tu numero: "))

def multiplicar(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    

multiplicar(n)

