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
# both the class attribute and the obj, when they try to access the class attribute, they point to the same memory addr
# Its not possible to change the class attr throught the obj of this class