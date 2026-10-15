#class for taking name and marks
class Student:
    def __init__(self, name, bio, phy, chem):
        self.name = name
        self.bio = bio
        self.phy = phy
        self.chem = chem

    def get_avg(self):
        sum = self.bio + self.phy + self.chem
        print(sum/3)

s1 = Student("Khelemba", 88, 90, 77)
print("Average marks is: ", end="")
s1.get_avg()

#account and balance
class Account:
    def __init__(self, balance, account_no):
        self.balance = int(balance)
        self.account_no = int(account_no)

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debitted from your account", self.account_no)
        print("Total balance is: ", self.get_bal())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited to your account no", self.account_no)
        print("Total balance is: ", self.get_bal())

    def get_bal(self):
        return self.balance
    
acc = Account(10000, 19052006)
acc.credit(5000)
acc.debit(2500)