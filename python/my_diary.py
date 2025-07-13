

def my_contacts():
    my_contacts = {}
    while True:
        print("Bienvenido a tu agenda de contactos")
        option = input("Escoge la opcion  que desees llevar a cabo:\n b : Buscar contacto\n a: Agregar contacto\n ac : Actualizar contacto\n e : eliminar contacto\n S: Salir\n")

        if option == "a":
            print("Usted selecciono agrgar contacto, debe ser de 9 digitos")
            name = input("Ingrese el nombre: ")
            num = input("Ingresa el numero: ")
            if len(num) != 9 and type(num) != int:
                print("Selecciona un numero correcto")
            else: 
                my_contacts[name] = num
                print(f"El contacto se agrego con exito {my_contacts}")
        elif option == "b":
            print("Seleccionaste buscar contacto")
            name = input("Ingrese el nombre ")
            validation = name in my_contacts
            if validation == True:
                print(f"El numero de{name} es {my_contacts[num]}")
            else:
                print("Ese contacto no existe")
        elif option == "ac":
            print("Seleccionaste actualizar contacto")
            name = input("Ingrese al contacto que vas a cambiar de nombre")
            validation = name in my_contacts

            if validation == True:
                name = input("Ingrese el nombre nuevo: ")
                my_contacts[name] = num
                print(f"El nombre se cambio correctamente {my_contacts}")
            else:
                print("El contacto no existe")
        elif option == "e":
            print("Seleccionaste borrar contacto")
            name = input("Ingresa el nombre del contacto que deas eliminar")
            validation = name in my_contacts

            if validation == True:
                del my_contacts[name]
                print(f"{my_contacts[name]} se ha eliminado con exito")
            else:
                print("El contacto no existe")
        elif option == "S":
            print("Seleccionaste salir de tu agenda, a continuacion te mostraremos tus contactos")
            print(f"{my_contacts}")
            break

        else:
            print("No se ingreso correctamente")

my_contacts()