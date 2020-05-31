#Experiment 4, Program 4.1
#Program to implement Inheritance
from Exp301Copy import Student

class SECO(Student):
    courses=list()
    skills=list()
    def __init__(self):
        #Student.__init__(self)
        pass
    def setprop(self,c,s):
        self.setval('18CO01','FromDer','Mum',89989)
        self.courses.append(c)
        self.skills.append(s)
    def getprop(self):
        print(self.getval())
        print('Courses:',self.courses,'\nSkills:',self.skills)

s=SECO()
#print(s.getval())
#s1=SECO('18DCO01','Almas','Mumbai',9898989898)
#print(s1.getval())
s.setprop('OSTL','Python')
s.setprop('AOA','Design Algos')
print(s.getprop())


