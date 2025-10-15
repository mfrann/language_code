

'''

INTERVIENE DOS CLASES
PADRE / HIJA
para que hija herede, solo hay que pasar los atributos



ejmplo:
Padre: Pelirrojo, Ojos cafe, moreno

Hija: pelirrojo, ojos verdes, moreno

'''


class Vehiculo():
    def __init__(self, matricula, modelo, marca, color):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False


    def avanzar(self):
        self.avanza = True
    def frenar(self):
        self.frena = True
    def girar(self):
        self.gira = True 
    def imprimir(self):
        print(
            f' Matricula: {self.matricula} \n Modelo: {self.modelo} \n Marca: {self.marca} \n'
            f' Color: {self.color} \n Avanzar: {self.avanza} \n Frenar: {self.frena} \n Girar: {self.gira}'
            )      

class Moto(Vehiculo):
    pass

moto1 = Moto("ABC123", 2018, "BMW", "Azul") 
moto1.avanzar()
moto1.girar()
moto1.imprimir()


'''
Para agregar otro atributo se usa super().__init__(atributos)
y en el atributo principal def __init__(self, atributos)
'''