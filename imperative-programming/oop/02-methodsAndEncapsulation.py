# This is an employee class
# Methods are functions within the object, that encapsulates the logic.
# They can be called from other parts of the program, giving a very clean look.

# Here is an exemple
class Employee:
    # This is the init method. It creates an obj when its called, with or without the parameters to initialize
    def __init__(self, name, age=None, salary=None):
        self.name = name
        self.age = age
        self.salary = salary
        print(f"__init__ is called for object {id(self)}")

    def get_raise(self, bonus): 
        self.salary += bonus

    def get_name(self):
        return self.name
    
    def inc_age(self):
        self.age += 1
    
    def get_age(self):
        return self.age 

# this is the right way to call a method        
e1 = Employee("Alice")
e2 = Employee("Pedro", 40)

# it can be also called by the following, but it's not usual
# Employee.get_age(e1)

print(e1.get_name())
print(e1.get_age())

# encapsulation is having a well defined interface, between users and classes
# the implementations, for instance how it gona solve the problem, is private, but the method to be called is public
# it's like a black box, where only the class creator sees the logic, the user don't, just calls the method
# in python, using _ before the function, it is meant to be private, not recommended using