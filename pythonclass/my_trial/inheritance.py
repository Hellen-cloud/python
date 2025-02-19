#parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)

p1=Person("John", 36)
p1.printname()

#child class
class Person2(Person):
    pass
p2=Person2("John", 36)
p2.printname()
#Single Inheritance: A child class inherits from a single parent class.
#Multiple Inheritance: A child class inherits from more than one parent class.
#Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
#Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
#Hybrid Inheritance: A combination of two or more types of inheritance.