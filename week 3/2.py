class person(object):
    def __init__(self,name):
        self.name=name

    def getname(self):
        return self.name

    def isemployee(self):
        return False

class employee(person):
    def isemployee(self):
        return True

emp=person("slamet")
print(emp.getname(),emp.isemployee())
emp=employee("santoso")
print(emp.getname(),emp.isemployee())