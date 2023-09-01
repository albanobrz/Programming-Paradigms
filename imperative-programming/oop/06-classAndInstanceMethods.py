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