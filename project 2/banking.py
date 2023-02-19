class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Person details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Account balance has been updated: $ {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if (self.amount > self.balance):
            print(f"Insufficient Funds | Balance available: $ {self.balance}")
        else:
            self.balance = self.balance - self.amount
            print(f"Amount balance has been updated: $ {self.balance}")

    def view_balance(self):
        print(f"Actual balance: $ {self.balance}")