num=float(input("Enter a number the first number: "))
num1=float(input("Enter a number the second number: "))
operator=input("Enter a operator (+,-,*,/): ")

if operator=="+":
    results=num+num1
    print(f"The result of {num} {operator} {num1} is {results}")

elif operator=="-":
    results=num-num1
    print(f"The result of {num} {operator} {num1} is {results}")
elif operator=="*":
    results=num*num1
    print(f"The result of {num} {operator} {num1} is {results}")
elif operator=="/":
    if num1 != 0:
        results=num/num1
        print(f"The result of {num} {operator} {num1} is {results}")
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator!")

