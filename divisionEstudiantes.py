import sys
import random

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

    totalStudents = len(listStudents)
    totalGroups = int(groups)

    cantMembers = totalStudents // totalGroups
    restMembers = totalStudents % totalGroups

    randomGroup = random.sample(range(0,totalGroups),totalGroups)

    for g in randomGroup:
        for s in range(cantMembers):
            stu = random.randint(0,len(listStudents)-1)
            listGroups[g].members.append(listStudents[stu])
            del listStudents[stu]

    randomGroup2 = random.sample(range(0,totalGroups),restMembers)
    for g in randomGroup2:
        stu = random.randint(0,len(listStudents)-1)
        listGroups[g].members.append(listStudents[stu])
        del listStudents[stu]


    #repartir los temas

    totalTopics = len(listTopics)

    cantTopics = totalTopics // totalGroups
    restTopics = totalTopics % totalGroups
    
    randomGroup3 = random.sample(range(0,totalGroups),totalGroups)
    for g in randomGroup3:
        for s in range(cantTopics):
            top = random.randint(0,len(listTopics)-1)
            listGroups[g].topics.append(listTopics[top])
            del listTopics[top]

    randomGroup4 = random.sample(range(0,totalGroups),restTopics)
    for g in randomGroup4:
        top = random.randint(0,len(listTopics)-1)
        listGroups[g].topics.append(listTopics[top])
        del listTopics[top]

    for g in listGroups:
        print("##########################")
        print(g.name)
        print("Members:")
        print("\t" + str(g.members))
        print("Temas:")
        print("\t"+str(g.topics))
Code()
