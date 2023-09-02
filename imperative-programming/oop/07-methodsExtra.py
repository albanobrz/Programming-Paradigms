class Student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    @classmethod
    def fromFullname(cls, fullName):
        first, last = fullName.split(' ')
        return cls(first, last) # equivalent to Student(first, last), it creates a new instance
    
    @classmethod
    def fromJson(cls, json):
        #process json input
        return cls(first, last)

s1 = Student.fromFullname("Bob Ross")
print(type(s1), s1.firstName)

# The json exemple is great. I can create a new instance of an object using anything.
# I would have to process the json and provide the right input if I would use the intance method (init self)
# But with the class, its possible to provide the json and treat the json inside the method, getting exacly what I need to start an obj
# its very flexible, great