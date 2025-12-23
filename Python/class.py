#OOP - Object Oriented Programmig
# - organizing your code into objects 
# - combines data(properties), behaviour(method)
#Classes are blueprints of creating objects

#format
# class Name_of_the_class : 
#     #initialization function
#     def __init__(self, prop_one, prop_two):
#         self.prop_one = "anything"
#         self.prop_two = prop_two

#    #write your custom method
#     def name_of_method(self):
#     #execution statement

# Create an instance of a class
# name_of_variable = Name_of_the_class(pram_one, pram_two)     

 
class Student:
    def __init__(self, name, age) :
        self.name = name
        self.age = age


    def introduction(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")    

 #create instance of Student
femi = Student("Femi", 3)  
print(femi.introduction())     

# create a class called shape(side,color) and determine 
# if the shape is rectangle or not
class Shape:
    def __init__(self, sides, color):
       
        self.sides = sides
        self.color = color

    def is_rectangle(self):
        if self.sides == 4:
            print("This is a rectangle")
            
        else :
            print("This is not a rectngle") 

# add a method to find the area of the rectangle

    def area(self, length, width):
        return length * width
    
        
rectangle = Shape(4,"red")   
rectangle.is_rectangle()  
print(rectangle.area(5,3))
# Subclass - a class that inherits properties and method 
# of a superclass(parent class)
# it can over ride methods

#format of a subclass
# class Subclass(Super_class):
#     #initialization func
#     def __init__(self, subprop_one, subprop_two):
#         super().__init__(prop_one, prop_two)
#         #intializeothers
#     def area(self):
#         print("this is no longer area")


#create an Animal class, check if it is mammal or amphibian, reptiles

class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        
    def check_type(self):
        if self.animal_type == "mammal":
            return f"{self.name} is a mammal"
        
        elif self.animal_type == "amphibian":
            return f"{self.name} is a amphibian"
        
        elif self.animal_type == "reptile":
            return f"{self.name} is a reptile" 

        else :
            return f"{self.name} is not in the list"   
        

check = Animal("lion", "mammal")
print(check.check_type())


#create a subclass a Lion Subclass and over ride the check, 
# and tell us the sound it makes

class Lion(Animal):
    def __init_subclass__(self, sound):
        super().__init__(name , animal_type)
        self.sound = sound
        
        
    def check_type(self) :  
        if self.sound == "grrr":
            return f"{self.sound} is the sound of Lion"

A = Lion("grrr", ) 
print(A.check_type())





