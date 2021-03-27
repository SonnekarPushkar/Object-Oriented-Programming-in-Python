#                                 || OBJECT ORIENTED PROGRAMMING ||
#                                             |CLASS|
'''
class number:
    def sum(self):
        return self.a + self.b

num = number() --> number instantiation
num.a = 12
num.b = 34
s = num.sum()
print(s)
'''
'''
class RailwayForm:
    formtype = "Railway Form"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
harrysApllication = RailwayForm()
harrysApllication.name = "Harry"
harrysApllication.train = "Nandigram"
harrysApllication.printData()
'''
'''
class Remote:
    pass

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        pass
#                                Made by Pushkar Girish Sonnekar
    def moveTop(self):
        pass
remote1 = Remote()
player1 = Player()
if(remote1.isLeftpressed()):
    player1.moveLeft()
'''
'''
class Employee:
    company = "Google"
    salary = 100 --> class attribute
pushkar = Employee()  
rajini = Employee() 
pushkar.salary = 300 --> instance attribute
rajini.salary = 400
print(pushkar.company)
print(rajini.company)
Employee.company = "Youtube"
print(pushkar.company)
print(rajini.company)
print(pushkar.salary)
print(rajini.salary)
'''
'''
The first priority would always be the instance attribute but if an instance attribute is not present,
then the priority would be class attribute.And if both aren't present then error is thrown.
'''
'''
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company}is {self.salary}")
harry = Employee()
harry.salary = 100000
harry.getSalary()
Employee.getSalary(harry)
'''
#Static method
'''
class temp:
    @staticmethod
    def greet():
        print("Good morning sir")
user = temp()
temp.greet()
'''
'''
class Time:
    @staticmethod
    def time():
        print("The time is 9 am in the morning")
harry = Time()
harry.time()
'''

#                                        |CONSTRUCTOR|
'''
class Employee:
    company = "Google"
    def __init__(self, name, salary , subunit):
        self.name = name
        self.subunit = subunit
        self.salary = salary
        print("Employee is created")
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The subunit of the employee is {self.subunit} ")
        print(f"The salary of the employee is {self.salary}")
pushkar = Employee("Harry",1000,"Search function")
pushkar.getDetails()
'''

#                                       |PRACTICE SET|
'''
class programmar:
    def __init__(self, name , salary , id):
        self.name = name
        self.salary = salary
        self.id = id
    def getInfo(self):
        print(f"Name of the programmar is {self.name} . His / Her salary is {self.salary} and ID is {self.id}")

person1 = programmar("Pushkar", 90000 , 5428665)
person2 = programmar("Pratham", 90000 , 5428666)
person1.getInfo()
person2.getInfo()
'''
