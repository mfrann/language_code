

#CONDICIONALES

"""

IF: evalua la condicion (imprescindible)

ELSE: especifica que hacer si no se cumple la condicion 
(opcional)

ELIF: SI NO PASA ESTO, QUE PASE ESTO OTRO

"""


#CONDICIONAL IF / ELSE

#EJEMPLO 

#CREA UN PROGRAMA QUE DIGA CUANTOS ANOS TIENES MI COMPUTADORA
#DECIR SI ES NUEVO VIEJO
# SI ES MENOR O IGUAL A 2, ENTONCES ES NUEVO
#PERO SI ES MAYOR QUE 2, ENTONCES ES VIEJO

"""
age_pc = int(input("Years of ur computer: "))

if age_pc >= 0 and age_pc <= 2:
    print("Es nueva !!!")
else:
    print("Es vieja :c")
"""


age = int(input("Your age?: "))

if age <= 18:
    print("No Ingresas")
else:
    print("Ingresas")


#CONDICIONAL ELIF

"""
ESCUELA DE CONDUCCION, SE TIENE UN PROGRAMA 
DE LA EDAD DEL USUARIO

SI ES MENOR A 16 NO CONDUCE
SI ES MENOR A 18 PIDE PERMISO

"""


user = int(input("User: "))

if user < 16:
    print("No puedes conducir")
elif user < 18:
    print("Pueder tener un permiso")
else:
    print("Tienes tu licencia")
