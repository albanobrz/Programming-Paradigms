class Employee:
    def get_raise(self, bonus): 
        self.salary += bonus

    def get_name(self):
        return self.name
    
    def inc_age(self):
        self.age += 1
    
    def get_age(self):
        return self.age

e1 = Employee()

e1.name = "Alice"
e1.age = 25
e1.salary = 10000

print(f"Alice salary before bonus is {e1.salary}")

# wrong way
Employee.get_raise(e1, 2000)

# right way
e1.get_raise(2000)

print(f"Alice salary after bonus is {e1.salary}")
print(e1.get_name())