# magic methods are the methods that all objects(variables) have in python
# for instance the int 5, has the __add__ method. (dir(5) to see)
# the __add__ is a function that is used in + operator
# I can use the x = 5 -> x.__add__(1) -> 6

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def prettyPrint(self):
        if self.imag == 0:
            print(self.real)
        elif self.imag > 0:
            print(f"{self.real}+{self.imag}i")
        else:
            print(f"{self.real}-{-self.imag}i")
            
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r, i)
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

c1 = ComplexNumber(2, 2)
c2 = ComplexNumber(2, 2)
# c3 = c1.add(c2)
c3 = c1 + c2
c3.prettyPrint()

print(c1 == c2)

# in the code above, the __add__ was override to this class
# Now its possible to use the + operator, and it will work to add the complex number
