# create a program that finds the largest of three numbers

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is greater")
elif num2>num3 and num2>num1:
    print(f"{num2} is greater")

else:
    print(f"{num3} is greater")
