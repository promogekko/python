class Employee:
#'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

#--------------------------------------------------------------------

class Foo:
    def __init__(self):
        pass

    def __privateMethod(self):
        return 3

    def invoke(self):
        return self.__privateMethod()

#--------------------------------------------------------------------
emp1 = Employee("Zara", 2000)
emp2 = Employee("Bob",5000)
emp3 = Employee('Thomas',7000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print("Total Employee %d" % Employee.empCount)

setattr(emp1, 'age', 8) # Set attribute 'age' at 8
hasattr(emp1, 'age') # Returns true if 'age' attribute exists
getattr(emp1, 'age') # Returns value of 'age' attribute
print(dir(emp1))
#delattr(empl, 'age') # Delete attribute 'age'

# __new__ est une methode static, alors que __init__ est methode d'instance.  __new__ doit creer l'instance en premier,  __init__ peut l'initialiser.
#  A noter __init__ prend self comme parametre
# __new__ cree l'objet self







#=========== foo ------------------------

f = Foo()
print(f.invoke())
print(dir(f))
print(f.__privateMethod())
