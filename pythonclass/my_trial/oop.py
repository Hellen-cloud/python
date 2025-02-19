class Trial:
      fact="Just a trial."
      def __init__(self,name,age,gender,salary):
       self.name=name
       self.age=age
       self.gender=gender
       self.salary=salary

p1= Trial("Joshua",22,"Male",200000)
print(p1.name,p1.age,p1.gender,p1.salary)#instance variable
print(p1.age)#instance variable
print(p1.gender)#instance variable
print(Trial.fact)#class variable
print(p1.fact)#instance variable

#Modify instance variables
p1.name="Migael"
print(p1.name)

#Modify class variable
Trial.fact="Jesus loves you"
print(p1.fact)
print(Trial.fact)


