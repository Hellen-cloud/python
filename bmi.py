# create a program that can calculate your bmi
import sys

weight=float(input("Enter your weight(kg):"))
if weight > 180:
    print("Your weight is invalid")
    sys.exit()

height1=float(input("Enter your height(m):"))
height2=float(input("Renter your height(m):"))

if height1 > 2.72 and height2 > 2.72:
    print("Your height is invalid")
    sys.exit()
height=height1*height2
bmi=weight/height
if weight/height >7.6 and weight/height<18.5:
    bmi=weight/height
    print(f"Your BMI is {bmi};therefore you are underweight")

elif weight/height >=18.5 and weight/height <25:
    bmi=weight/height
    print(f"Your BMI is {bmi};therefore you are healthy")
elif weight/height >=25.0 and weight/height <30:
    bmi=weight/height
    print(f"Your BMI is {bmi};therefore you are overweight")
elif weight/height >=30.0 and weight/height <40:
    bmi=weight/height
    print(f"Your BMI is {bmi};therefore you are obese")

elif weight/height >=40 and weight/height <60:
    bmi=weight/height
    print(f"Your BMI is {bmi};therefore you are severely obese!")
else:
    print("Invalid input")
    sys.exit()




