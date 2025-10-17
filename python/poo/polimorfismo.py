


'''
PILAR DE LA POO JUNTO CON LA HERENCIA

Muchas formas: objetos toman diferentes formas

Ejm.
Gato: 
    Salvaje
        acariciar() -> rabia
    Domesticado
        acariciar() -> alegria

'''

class Perro():
    def sonido(self):
        print("GUAU")

class Gato():
    def sonido(self):
        print("MIAU")

class Cerdo():
    def sonido(self):
        print("OINK")

def onSonido(animal):
    animal.sonido()

gato = Gato()
perro = Perro()
cerdo = Cerdo()


onSonido(cerdo)