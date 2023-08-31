class Employee:
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
        
e1 = Employee("Alice")
e2 = Employee("Pedro", 40)
print(e1.get_name())
print(e1.get_age())