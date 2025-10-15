

#PARAMETROS POSICIONALES

'''

*args: 
-para pasar de forma opcional distintos valores
-puede ir otro nombre pero si usa *

def datos_usuario(name,age,city):
--> def datos_usuario(*args):
        print(args)     

datos_usuario('Paola', 24, 'Lima')



**kwargs
-por convencion
-distintos valores pero variables con nombre
-se trabaja con base de datos, filtrar informacion


def datos_usuario(**kwargs):
    print()

datos_usuario(name=Paola, etc)
'''


#EJEMPLOS
'''
def suma(*args):
    s = 0

    for i in args:
        s += i
    return s


result = suma(2, 5, 7, 19, 0, 67, 21)

print(result ** 2)



def lenguaje(nombre, *args):
    print(f'Hola {nombre}')
    print(f'Tus lenguajes favoritos son: {args}')


lenguaje("Martin", "JavaScript", "Python")
'''

def lenguaje(nombre, **kwargs):
    print(f'Hola {nombre}')
    print(f'Buscando informacion acerca de tus lenguajes...')
    print(f'Cargando informacion...')
    print(f'Informacion: ')

    contador = 0

    for key in kwargs:
        contador +=1
        print(f'Tu {contador}  favorito es: {kwargs[key]}')
    
lenguaje("Eduardo", lenguaje1="Ruby", lenguaje2="Python", lenguaje3="JavaScript")


