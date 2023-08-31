# encapsulation is having a well defined interface, between users and class
# the implementations, for instance how it gona solve the problem, is private, but the method to be called is public
# remember the black box
# in python, using _ before the function, it is meant to be private, not recommended using

from employee import Employee

e1 = Employee('Alex', 25, 'junior')
print(e1.age)