class Employee:
    pass

e1 = Employee()
e2 = Employee()
print(type(e1))

e1.name = "Alice"
e1.age = 25
e1.salary = 10000

e2.name = "Bob"
e2.age = 30
e2.salary = 20000

print(f'e1 name is: {e1.name}, e2 name is: {e2.name}')
print(f'e1 age is: {e1.age}, e2 age is: {e2.age}')
print(f'e1 salary is: {e1.salary}, e2 salary is: {e2.salary}')
e1.age += 1
print(f'e1 age is: {e1.age}')

# interesting thing, int, str, array are imutable. If I do

# x = 5
# y = x

# still same number and same memory address

# but if I do 

# y = y + 1

# x will continue as it was originally, and y will point to another memory address

# but for dictionary, or other types, it doesnt happen

# if I go for 

# e2 = e1
# e2.name = "newName"

# it will affect both, and python will not create a new space in memory, because this structure is mutable