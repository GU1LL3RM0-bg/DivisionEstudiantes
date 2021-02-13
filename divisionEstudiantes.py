import sys


#crear una clase grupo: nombre, lista estudiantes, lista temas


class Group:

    def __init__(self,name,members,topics):

        self.name = name
        self.members = members
        self.topics
        
#verificacion de la entrada

try:
    students = sys.argv[1]
    topics = sys.argv[2]
    groups = sys.argv[3]
except:
    print("La cantidad de parametros introducidos por consola es incorrecta")
    print("Ej: $divisionEstudiantes.py est.txt temas.txt #entero")
    sys.exit(1)
#crear las listas

#repartir los estudiantes

#repartir los temas
