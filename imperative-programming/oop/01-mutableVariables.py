# MUTABLE AND IMUTABLE VARIABLES

# The concept of imutable and mutable variables is important to know before OOP. 
# Variables of type int, str, array, tuples, booleans are considered imutable.

x = 5
y = x

print(y)
print("y address", id(y))
print("x address", id(x))

# y will be the same number and same memory address than x
# but if I do 

y = y + 1

print(y)
print("y address", id(y))

# x will continue as it was originally, and y will point to another memory address.

# but for dictionary, objects or other types, it doesnt happen...

class Employee:
    pass

e1 = Employee()
e2 = Employee()

e2 = e1
e2.name = "newName"

print("employee 1", id(e1))
print("employee 2", id(e2))

# it will affect both, and python will not create a new space in memory, because this structure is mutable


# METHODS IN OOP

