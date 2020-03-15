class Employee:
    empNo = 0
    def __init(self, name = ""):
        self.number = Employee.empNo
        Employee.empNo += 1
        self.name = name

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number
    empNumber = property(getNumber, setNumber)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    empName = property(getName, setName)


class Nurse(Employee):
    def __init__(self, name = "", type = "practical"):
        Employee.__init__(self, name)
        self.type = type

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type
    NType = property(getType, setType)


class Doctor(Employee):
    def __init__(self, name = "", expertise = "heart"):
        Employee.__init__(self, name)
        self.expertise = expertise

    def getExpertise(self):
        return self.expertise

    def setExpertise(self, expertise):
        self.expertise = expertise
    DExpertise = property(getExpertise, setExpertise)
class Supervisor(Doctor):
    def __init__(self,name, expertise,supervisees = []):
        Doctor.__init__(self,name,expertise)
        self.supervisees = supervisees
    def getSupervisees(self):
        return self.supervisees
    def setSupervisees(self,supervisees):
        self.supervisees = supervisees
    SuperviseesList = property(getSupervisees,setSupervisees)
    def addSupervisee(self,employee):
        self.supervisees.append(employee)
    def removeSupervisee(self,employee):
        self.supervisees.remove(employee)