#oop stands for Object Oriented Programming
#a class is a blueprint of an object
#an object is an instance of a class

class Student:
    #constructor method
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    #Member Function
    def display(self):
        print(f"Student name is {self.name},Age is {self.age},Score is {self.score}")

#instance of a class(object)
myobj=Student("Hellen",18,"A")
myobj.display()
myobj2=Student("Migael",22,"B")
myobj2.display()
myobj3=Student("Sheila",27,"A")
myobj3.display()
myobj4=Student("Nathan",18,"B")
myobj4.display()
myobj5=Student("Leila",23,"A")
myobj5.display()


