
'''
para que sea privado:
self._proyecto = proyecto


Clase: "¿Necesito que este 'objeto' 
tenga memoria y comportamiento?"

Función: "¿Puedo hacer esto sin recordar 
nada entre llamadas?"

'''

#EJEMPLO

class Persona:
    def __init__(self, identificacion, nombre, edad):
        self.__identificacion = identificacion
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return "Hola ", self.nombre
    
    def getIdentificacion(self):  #para tener dato privado
        return self.__identificacion
    
    def setIdentificacion(self, valor): #para 
        self.__identificacion = valor

persona1 = Persona(61143, "Martin", 18)
print(persona1.saludo())
#print(persona1._Persona__identificacion) #para imprimir dato privado
persona1.setIdentificacion(12345)
print(persona1.getIdentificacion()) #otra forma de obtener un dato privado
print(persona1.edad)
