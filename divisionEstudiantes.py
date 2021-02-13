import sys


#crear una clase grupo: nombre, lista estudiantes, lista temas


class Group:

    def __init__(self,name,members,topics):

        self.name = name
        self.members = members
        self.topics = topics
        
#verificacion de la entrada

try:
    students = sys.argv[1]
    topics = sys.argv[2]
    groups = sys.argv[3]
except:
    print("La cantidad de parametros introducidos por consola es incorrecta")
    print("Ej: $divisionEstudiantes.py est.txt temas.txt #entero")
    sys.exit(1)

def Code():
    #crear las listas
    listStudents = []
    listTopics = []
    listGroups = []

    with open(students)as fileStu:
        for s in fileStu.read().split("\n"):
            listStudents.append(s)
        fileStu.close()
    with open(topics) as fileTop:
        for t in fileTop.read().split("\n"):
            listTopics.append(t)
        fileStu.close()
    for i in range(int(groups)):
        g = Group("Group#"+str(i+1),[],[])
        listGroups.append(g)
           
    

    #repartir los estudiantes


    #repartir los temas

Code()
