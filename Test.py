class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

y = person("John","Doe") 

y.printname()

class Student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname,self.lastname,"to the class of", self.graduationyear)

x = Student("Antonio","Winn",2020)

x.welcome()