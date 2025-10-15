

#CICLO WHILE

#REVISA LA CONDICIION SI ES VERDADERA, SE 
#EJECUTA HASTA QUE SEA FALSA
'''

while condition:
    cuerpo de bucle

'''

#EJEMPLO

contador = 0

while contador != 2:
    contador = int(input("Seguir calculando el imc? Si(1) No(2) "))

    if contador == 1:
        estatura = float(input("Cual es tu estatura?: "))
        peso = float(input("Cual es su peso?: "))
        resultado = round(peso/(estatura**2), 2)

        if resultado < 18.5:
            print(f'IMC {resultado} = BAJO DE PESO')
        elif 18.5 < resultado < 24.99:
            print(f'IMC {resultado} = PESO NORMAL')
        elif 25 < resultado < 30:
            print(f'IMC {resultado} = SOBRE PESO')
    else: 
        print("Gracias")