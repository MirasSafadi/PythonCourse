class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    PName = property(getName,setName)       
    def getIDNumber(self):
        return self.idnumber
    def setIDNumber(self,id):
        self.idnumber = id
    ID = property(getIDNumber,setIDNumber)
    def display(self):
        print(self.name)
        print(self.idnumber)
    @staticmethod
    def domSomething():
        print("this is a test for static method")
class Employee(Person):
    def __init__(self, name = "", idnumber = 0, salary = 100, post = ""):
        self.salary = salary
        self.post = post
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
    def getSalary(self):
        return self.salary
    def setSalary(self,salary):
        self.salary = salary
    Esalary = property(getSalary,setSalary)
    def getPost(self):
        return self.post
    def setPost(self,post):
        self.post = post
    Epost = property(getPost,setPost)
    def display(self):
        super().display()
        print(self.salary)
        print(self.post)
    @staticmethod
    def domSomethingElse():
        print("this is a test for static method in other class")


# creation of an object variable or an instance
a = Person('Yousef', 2277655)
# calling a function of the class Person using its instance
a.display()
b = Employee() # all attributes get default values 
# demonstrating the use of properties

# print(b.Pname)
b.PName = "Miras"
b.ID = 22668855
b.Esalary = 40000
b.Epost = "intern"
b.display()

Person.domSomething()
Employee.domSomethingElse()

