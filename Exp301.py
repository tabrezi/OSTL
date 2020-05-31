#Experiment 3, Program 3.1
#Program to implement Class, objects and static method

class Student:
    '''
    A student class to manage students.
    '''
    no_of_courses=5     #class var
    credits=25          #class var
    
    def setval(self,r,n,a,m):
        '''
        Method to set the properties of the object.
        '''
        self.rollno=r      #instance var
        self.name=n
        self.addr=a
        self.mob=m
    def getval(self):
        print('Self is at',id(self))
        return self.rollno, self.name, self.no_of_courses, self.credits, self.mob
    @classmethod
    def setcourses(cls,n):
        cls.no_of_courses=n
    @classmethod
    def setcredits(cls,c):
        cls.credits=c
    @staticmethod
    def is_workday(day):
        if day.weekday()==6:
            return False
        return True

s1=Student()
s1.setval('18CO01','Ansari Adeeba','Mumbai',9898998989)
print('s1 is at',id(s1))

print(s1.getval())
#print(s1.setval.__doc__)

s2=Student()
#Student.setcourses(6)
s2.no_of_courses=6
print('s2 is at',id(s2))

s2.setval('18CO02','Karia Janvi','Mumbai',9898998989)
#print('s2 is at',id(s2))
print(s2.getval())
print(s1.getval())
print(s1.__dict__)
print(s2.__dict__)

Student.setcredits(30)
print(s1.getval())
print(s2.getval())


import datetime
d=datetime.date(2020,2,23)
print('Is workday ?',Student.is_workday(d))
