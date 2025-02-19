# list data structure
# its ordered
# its mutable
# its has index

fruits=["Mangoes","Bananas","Apples","Grapes"]
print(fruits)
fruits[1]="Peach"
print(f"I love eating {fruits[1]}")


numbers=[13,2,3,4,43,8,7,12,9]
numbers.sort()
numbers.append("Pineapples")
numbers.pop()
numbers.reverse()
print(numbers[0])
print(numbers)

# tuple data structure
# its ordered
# it has index
# it's immutable'


cars=("Porshe","G-Wagon","Mazda","BMW","Ferari","Buggati")
nambari=(3,7,1,2,4,7,78,8)
# cars[5]="Subaru"

print(cars)
print(f"Germany produces {cars[3]}")
print(nambari)
print(sorted(nambari))


# set data structure
# not ordered
# no index

country={"Kenya","Seychelles","Madagascar","Morocco","Rwanda","Australia"}
print(country)
country.pop()
print(country)

# dictionary datastructure
# its mutable
students={"Name":"Hellen","Age":18,"Gender":"Female","Phone number":+254787887667}
students['Name']="Ann"
print(f"My name is {students['Name']} and I am {students['Age']} years old.My gender is {students['Gender']} and my phone number is {students['Phone number']}.")
