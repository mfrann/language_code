

#DICCIONARIO

'''

diccionario = {
    "Nombre": "Sara",
    "Edad": 23,
    "Documento": 61143283
}

print(diccionario)

diccionario_2 = dict(
    Nombre='Paola',
    Edad=37,
    Documento=61143283
)

print(diccionario_2)

diccionario_3 = dict([
    ('Nombre', "Jose"),
    ("Edad", 21),
    ("Documento", 901112)
])

print(diccionario_3)

'''

#

inventario = {
    "Manzana": 230,
    "Peras": 100,
    "Sandias": 500
}

print(inventario.keys()) #--> Manzana, Peras, Sandias
print(inventario.values()) #--> valores
print(inventario.items()) #-->ambos