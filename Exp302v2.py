#Experiment 3, Program 3.2
#Program to implement Constructors

class Student:
    no_of_courses=5
    credits=25
    def __init__(self,*args):
        if args.__len__()==0:
            self.rollno=self.name=self.addr=None
            self.mob=None
        elif isinstance(args[0],Student):
            self.rollno=args[0].rollno
            self.name=args[0].name
            self.addr=args[0].addr
            self.mob=args[0].mob
        else:
            self.setval(args[0],args[1],args[2],args[3])
    def setval(self,rollno,name,addr,mob):
        self.rollno=rollno
        self.name=name
        self.addr=addr
        self.mob=mob
    def getval(self):
        #print('Self is at',id(self))
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


'''
s1=Student()
s1.setval('17CO01','Ansari Heena','Mumbai',9898998989)
#print('s1 is at',id(s1))
print(s1.getval())
s2=Student()
Student.setcourses(6)
Student.setcredits(30)
s2.setval('17CO02','Iqra','Mumbai',9898998989)
#print('s2 is at',id(s2))
print(s2.getval())
s3=Student('17CO35','SS','M',9898)
print(s3.getval())
#type(s3)
s4=Student(s1)
print(s4.getval())
#import datetime
#d=datetime.date(2019,1,28)
#print('Is workday ?',Student.is_workday(d))
'''