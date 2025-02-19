# create a new file oop2.py file, then create a class called Cars with
# make,model,color ,yom as the the attributes in a constructor method. the a
# member function that prints(,,.....). finally create 5 object of the above
class Cars(object):
    def __init__(self, make, model, year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display(self):
        print(f"This car is made by {self.make},it is a {self.model},it was manufactured in the year {self.year} and it is {self.color} in color.")

car1=Cars("BMW","Convertable",2024,"Beige")
car1.display()
car2=Cars("Honda","SUV",2023,"Black")
car2.display()
car3=Cars("Ferari","Sports Car",2025,"Marron")
car3.display()
car4=Cars("Jeep","Crossover",2023,"Pink")
car4.display()
car5=Cars("Ford","Hatchback",2023,"Lime Green")
car5.display()
