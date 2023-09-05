# what is inheritance solving?
# removes redundancy and allow to define relationship between the classes

class Person:
    def __init__(self, firstName, lastname):
        self.firstName = firstName
        self.lastName = lastname
        
    def info(self):
        print(f"{self.firstName} {self.lastName}")

class Employee(Person):
    def __init__(self, first, last, id, salary):
        self.firstName = first
        self.lastName = last
        self.employee_id = id
        self.salary = salary    
    
    def info(self):
        print(f"{self.firstName} {self.lastName} {self.employee_id} {self.salary}")
        
p = Person("Leo", "Messi")
e = Employee("Fred", "Guedes", 1, 1000)

p.info()
e.info()


# all the methods, everything, including  __init__ from Person, will be inherited to Employee

# method overriding
# if you define in the inherited class (Employee for instance) a method that has the same name to the Person class method
# this method when called from the employee, will get the override

# using SUPER

class Person:
    def __init__(self, firstName, lastname):
        self.firstName = firstName
        self.lastName = lastname
        
    def info(self):
        print(f"{self.firstName} {self.lastName}")

class Employee(Person):
    def __init__(self, first, last, id, salary):
        super().__init__(first, last)
        self.employee_id = id
        self.salary = salary    
    
    def info(self):
        super().info()
        print(f"{self.employee_id} {self.salary}")
        
    def getRaise(self):
        self.salary = self.salary * 1.05
        
class LowPerformingEmployee(Employee):
    def getRaise(self):
        self.salary = self.salary * 1.01
        
    def info(self):
        super().info()
        print("Low performing Employee")

class HighPerformingEmployee(Employee):
    def getRaise(self):
        self.salary = self.salary * 1.1
        
    def info(self):
        super().info()
        print("High performing Employee")
        
class AveragePerformingEmployee(Employee):
    def info(self):
        super().info()
        print("Average performing Employee")
        
e = LowPerformingEmployee("Fred", "Guedes", 1, 1000)

e.info()
e.getRaise()
e.info()

o = object()
print(dir(o))

# always when overriding the original class and duplicated code, super should be used
# super gets the call of the original class, its clean and removes duplicated code

# in the code above, everything is being called from the info because:
# the super calls the employee calls, and the info on employee has the super that calls the info in person
