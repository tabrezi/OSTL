#Experiment 3, Program 3.1
#Program to implement Class, objects and static method

class Student:
    '''
    A Student class to maintain students information.
    It has class variables and also instance variables.
    '''
    no_of_courses=5     #class var
    credits=25          #class var
    
    def setval(self,rollno,name,addr,mob):
        '''
        Method to set the properties of the object.
        '''
        self.rollno=rollno      #instance var
        self.name=name
        self.addr=addr
        self.mob=mob
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

def main():

    s1=Student()
    s1.setval('17CO01','Ansari Heena','Mumbai',9898998989)
    #print('s1 is at',id(s1))
    print(s1.getval())
    #print(s1.setval.__doc__)
    s2=Student()
    Student.setcourses(6)

    s2.setval('17CO02','Iqra','Mumbai',9898998989)
    #print('s2 is at',id(s2))
    print(s2.getval())
    Student.setcredits(30)
    print(s1.getval())

    import datetime
    d=datetime.date(2019,2,11)
    print('Is workday ?',Student.is_workday(d))

if __name__=='__main__':
    main()
    