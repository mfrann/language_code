

'''
Seguridad informatica : 5.0
Ing. Web : 4.5 
IA : 3.6
Programacion Movil: 3.9 
Redes : 4.3


Programa solicite: 
nombre 
nombre materias
calificacion cada una

Da de resultado:
Nombre
Promedio
'''

print("Semestre 1")

name = input("Tu nombre completo: ")
materias = 5
notas = [5, 4.5, 3.6, 3.9, 4.3]
cursos = [
    "Seg. Informatica",
    "Ing. Web",
    "IA",
    "Programacion Movil",
    "Redes"
]

print("Tus cursos son: ")

for i in range(len(cursos)):
    print(f'{cursos[i]} : {notas[i]}')

#PROMEDIO
promedio = sum(notas) / len(notas)

print("RESULTADO")
print(f'Nombre: {name}')
print(f'Promedio: {promedio: .2f}')

