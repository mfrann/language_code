

#CONJUNTOS

'''
add //anade un elemento
clear //elimina toda informacion
pop //devuelve y elimina un elemento arbitrario o error si esta vacio
remove //intenta eliminar un elemento del conjunto o da error
union //devuelve un conjunto con todos los elementos de
ambos conjuntos

DEVUELVE EN DESORDEN

'''

#1 FORMA DE CONJUNTOS

alumnos = {
    'Andrea',
    'Camila',
    'Thalia',
    'Jordan',
    'Martin'
}

print(alumnos)

#2 FORMA 
lenguajes = set(['PHP', 'JAVA', 'C'])

#lenguajes.add("PYTHON") #NO PERMITE AGREGAR MAS DE UNO
#lenguajes.clear()
#lenguajes.pop()
lenguajes.remove("PHP")

todos = alumnos.union(lenguajes)

print(todos)