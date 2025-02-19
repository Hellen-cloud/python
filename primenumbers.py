num1=int(input("Enter a number: "))

if num1 <= 1:

    is_prime=False
elif num1 == 2:
    is_prime=True
else:
    is_prime=True
    for i in range(3, int(num1**0.5) + 1, 2):
        if num1 % i == 0:
            is_prime=False
            break
if is_prime:
    print(f"{num1} is a prime number")
else:
    print(f"{num1} is not a prime number")