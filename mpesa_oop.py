#define the user class
class User:
    def __init__(self,user_id,name,phone):
        self.user_id = user_id  #initialise user Id
        self.name = name   #initialise username
        self.phone = phone  #initialise phone number
        self.account=Account(self)   #creating an account for the user


    def __repr__(self):
        return f"User ({self.user_id} {self.name} {self.phone})"  #Representation of user Object

class Account:
    def __init__(self,user):
        self.user = user
        self.balance=0.0

    def deposit(self,amount):
        if amount > 0:     #check if the deposit is more than zero
            self.balance += amount
            print(f"{amount} deposited.New balance: {self.balance}")


        else:
            print("Deposited Amount must be greater than 0")

    def withdraw(self,amount):
        if 0< amount <= self.balance:  #checking the withdrawal amount is valid
            self.balance -= amount
            print(f"{amount} withdrawn.New balance: {self.balance}")

        else:
            print("Insufficient funds or Invalid amount")

    def __repr__(self):
        return f"Account ({self.user.name}, balance: {self.balance})"     #representation of account object

#define transaction class
class Transaction:
    def __init__(self,account,amount,transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def process(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)

        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)

        else:
            print("Invalid transaction type")

    def __repr__(self):
        return f"Transaction  Account {self.account.user.name}, Amount: {self.amount},Type: {self.transaction_type}"

# example usage // object/user1
user1=User(1,"Hellen Gaceri",740123467)
print(user1)

#deposit amount
user1.account.deposit(1000)


user1.account.withdraw(500)

transaction1=Transaction(user1.account,200,"deposit")
transaction1.process()

transaction2=Transaction(user1.account,100,"withdraw")
transaction2.process()

print(user1.account)

#user2
user2=User(2,"Melina Hershy",734236587)
print(user2)

user2.account.deposit(10000)

user2.account.withdraw(3000)

transaction3=Transaction(user2.account,4500,"deposit")
transaction3.process()

transaction4=Transaction(user2.account,2200,"withdraw")
transaction4.process()

print(user2.account)

#user3
user3=User(3,"Andrew Mekka",743679809)
print(user3)

user3.account.deposit(20000)

user3.account.withdraw(6500)

transaction4=Transaction(user3.account,40000,"deposit")
transaction4.process()

transaction5=Transaction(user3.account,22000,"withdraw")
transaction5.process()

print(user3.account)
