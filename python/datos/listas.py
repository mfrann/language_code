 

#LISTAS 
'''
Contenedor que aloja distintos datos

primera posicion es 0 -> indice



countries = ['Lima', 'New York', 'Buenos Aires', 'CDMX']

print(countries[2])

number =[]

for i in range(6):
    number.append(int(input("Introduce un numero: ")))

number.sort()
print(f'Los numeros ganadores son: {number}')

'''

#METODOS PARA ELIMINAR
''''
list = [1, 34, 54, 'Hola']

for i in list:
    print(i)

#list.remove(1) #valor
#list.pop(2) #posicion
#list.clear()
'''

#SI SE REPITE
list = [1,1,3,5,5]
print(list.count(1)) #contar cuanto se repite

print(list.index(3)) #en que ligar se encuentra

list.reverse() #reversa

print(list)