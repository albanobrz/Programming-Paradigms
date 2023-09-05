class Apple:
    food_type = "fruit"
    calories_per_100_grams = 50
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    
    def defineCalories(self):
        return self.weight/100 * Apple.calories_per_100_grams

a1 = Apple("red", 200)

print(a1.defineCalories())

# the food_type in this case is a class attribute... it means every obj has this same attribute.
# but the color and weight differs for each obj.
# I can access the class attribute using Apple.food_type like this
# all the obj instanciated from the class, have the access to class attribute.
# both the class attribute and the obj, when they try to access the class attribute, they point to the same memory address
# Its not possible to change the class attribute throught the obj of this class


# Here is another exemple...

class Apple:
    food_type = "fruit"
    calories = 50
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    
    def setColor(self, color):
        self.color = color

    @classmethod
    def set_calories(cls, c):
        print(f"cls is of type {type(cls)} and id {id(cls)}")
        cls.calories = c
        
    @staticmethod
    def volume(r):
        return 4/3*3.14*(r**3)
        
a = Apple("red", 100)
print(f"Volume of apple with radius 3 is {a.volume(3)}")


# its possible to change the class attr using a.__class__.food_type for instance.
# difference between class methods and instance methods:
#     instance methods, the first argument points to the instance
#     class methods, the first argument points to the class
# class methods modify, read the class, its explicit, good to use. Different of using __class__

# the static method doesnt modify anything, the class or the instance... 
# so it doesnt need a pointing argument, its static, just does something
# it can be accessed throght the class or instance

# summiryzing:
#     instance methods use self as first arg
#     class methods use decorator @classmethod and cls as first arg
#     static methods use decorator @staticmethod and no pointer arg, its a helper function

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

# The json exemple is great. It's possible to create a new instance of an object using anything.
# It would have to process the json and provide the right input if the intance method was used. (init self)
# But with the class, its possible to provide the json and treat the json inside the method, getting exacly what is needed to start an obj
# its very flexible, great power.