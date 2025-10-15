'''

Escribir un programa que permita guardar
nombres y numeros de telefono

Menu:

1) Consultar: pide un nombre. Si el nombre 
se encuentra en la agenda, debe mostrar el 
teléfono, si no indicar que no existe.

(2) Añadir: pide un nombre. Si el nombre se 
encuentra en la agenda, indicar que ya existe, 
si no solicitar el número de teléfono.

(3) Modificar: pide un nombre. Si el nombre 
no está en la agenda, indicar que no existe, 
sino solicitar el nuevo número de teléfono.

(4) Borrar: pide un nombre. Si el nombre no 
está en la agenda, indicar que no existe, sino 
eliminar el número de teléfono.

(5) Salir: si el usuario digita el número 5, 
detener el ciclo.




Jose: 302944
Mario: 829455
Angel: 829405
Luis: 930594

'''


#1 DICCIONARIO

agenda = {
    "Jose": 302944,
    "Mario": 829455,
    "Angel": 829405,
    "Luis": 930594
}

consultando = True

while consultando:
    print("MI AGENDA")
    print("------------")
    print("1. Consultar \n 2. Añadir \n 3. Modificar \n 4. Borrar \n 5. Salir")

    opcion = ""

    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input(">>> ")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")

        if nombre not in agenda:
            print("Este nombre no existe en la agenda")
        else:
            telefono = agenda[nombre]

            print(nombre, ":", telefono)

    elif opcion == "2":
        nombre = input("Ingrese nombre: ")

        if nombre in agenda:
            print("Este nombre ya esta en la agenda")
        else:
            telefono = int(input("Ingrese el nuevo telefono: "))

            agenda[nombre] = telefono

            print("El telefono se añadio correctamente")

    elif opcion =="3":
        nombre = input("Ingrese nombre: ")

        if nombre not in agenda:
            print("Este nombre no existe en agenda")
        else:
            telefono = int(input("Digite el telefono: "))
            agenda[nombre] = telefono
            print("El telefono se ha modificado correctamente")

    elif opcion == "4":
        nombre = input("Ingrese nombre: ")

        if nombre not in agenda:
            print("Este nombre no existe en la agenda")
        else:
            del agenda[nombre]
            print("El telefono se ha borrado correctamente")
    elif opcion == "5":
        consultando = False
        print("Gracias por utilizar el programa")
    else:
        print("Ocurrio un problema")
        consultando = False