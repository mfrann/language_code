

'''

CLASES: ANIMAL 

ATRIBUTOS: EDAD, PESO, NOMBRE
METODOS: CORREC, COMER, CAMINAR

OBJETOS:
GATO: Nombre=Na Edad=1 Peso=4kg
PERRO: etc..

'''

#EJEMPLO


class Bicicleta:
    def __init__(self, color, cambios, rin): #contiene los atributos
        self.color = color
        self.cambios = cambios
        self.rin = rin
    
    def frenar(self):
        return "La bicicleta esta frenando"
    def avanzar(self):
        return "La bicicleta esta en movimiento"
    def girar(self):
        return "La bicicleta esta girando"

urbana= Bicicleta("Azul", 8, 27.5)
hibrida = Bicicleta("Naranja", 1, 29)

print(urbana.color) #atributo no lleva parentesis
print(urbana.girar()) #metodo lleva parentesis

print("Urbana: " + str(urbana.color))
print("Comportamiento de la bicicleta urbana:  " + str(urbana.girar()))