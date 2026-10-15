#WAP to put the grades in a tuple and count how many students got A and then put them in a list and sort them in ascending order
Grades = ('C', 'D', 'A' , 'A' , 'B', 'B' ,'A')
a_count = Grades.count("A")
print("The numbers of students that got 'A': ", a_count)

list_Grades = list(Grades)
list_Grades.sort()
print(list_Grades)

#Sets and dictionaries
dict = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(dict)

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("the no. of classroom required :", len(subjects))

marks = {}
chem = int(input("enter chem marks: "))
marks.update({"chem" : chem})
phy = int(input("enter phy marks: "))
marks.update({"phy" : phy})
bio = int(input("enter bio marks: "))
marks.update({"bio" : bio})
print(marks)

val = {
    ("float", 8.0),
    ("int", 8)
}
print(type(val))


#For and while loops

#looping 1 to 100
num = 1

while num <= 100:
    print(num)
    num += 1


#looping 100 to 1
num2 = 100


while num2 >= 1:
    print(num2)
    num2 -= 1

#multiplication of n
n = int(input("Multiplication of : "))
var = 1


while var <= 10:
    print(n * var)
    var += 1


#printing the list with while loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0

while idx < len(nums):
    print(nums[idx])
    idx += 1


#finding a no. from the tuple
nums1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
a = 81
i = 0

while i < len(nums1):
    if (nums1[i] == a):
        print("Found a in :", i)
    i += 1


#printing the list with for loop
nm = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i  in nm:
    print(i)


#searching the tuple with for loop
nm1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 9
indx = 0

for i in nm1:
    if (i == x):
        print("found var in index", indx)
        
    indx += 1


#range
#print 1 to 100 using for and range
for _ in range(1, 101):
    print(i)



#print 100 to 1
for i in range (100, 0, -1):
    print(i)



#print the multiplication of number n
n = int(input("enter the multiplication number: "))

for i in range(1, 11):
    print(n * i)



#write a program to find the sums of first n numbers using while
n = int(input("enter numberss: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("total sum of 1 to the number is: ", sum)




#WAP to find the factorial of n number using for loop
m = int(input("enter factorial number: "))
fac = 1 #factorial need to start with 1

for i in range(1, m+1):
    fac *= i

print("the factorial number is : ", fac)



#WAF to print the length of a list
def len_list(var):
    print(len(var))

anime = ["Your Name", "Weathering with you", "Suzume"]
movies = ["Infinity war", "End game", "Far from home", "Brand New Day"]

len_list(anime)
len_list(movies)


#WAF to print the elements of a list
el1 = [1,3 ,2,3,4,6,4]
el3 = ["a", "b", "c", "d"]

def el_print(el):
    for i in el:
        print(i, end=", ")

el_print(el3)
print()


#WAF to find the factorial of n.
n = int(input("Enter the number: "))

def facto(n):
    fac = 1

    for i in range(1, n+1):
        fac *= i
    print(fac)

    #while fac <= n:
    #    sum *= fac  
    #    fac += 1
    #print(sum)

facto(n)  


#WAF to convert USD to INR
usd_sum = float(input("Enter USD amount: ",))

def conv(a):
    sum = a * 96.73
    print(sum, "INR")

conv(usd_sum)


#WAF to find even or odds
num = int(input("enter numbers: "))

def ev_odd(var):
    if (var/2 == 0):
        print(var, "is even")
    else:
        print("is odd")

ev_odd(num)

#Write a recursive function to calculate the sum of first n natural numbers
a = int(input("Enter natural number: "))

def re(n):
    if (n == 0):
        return 0
    else:
        return n + re(n-1)

print(re(a))


#Write a recursive function to print all elements in a list

def re1(n, idx=0):
    if (len(n) == idx):
        return
    else:
        print(n[idx])
        re1(n, idx + 1)

re1(movies)


#creating a new file and adding data to it
import os

#with open("practice.txt", "w") as f:
    #f.write("Hi everyone \nWe are learning File I/O \nUsing Java \nI like programming in Java")


#replacing all the word "java" with "python"
with open ("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python") 
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)


#searching if it has the word "learning"
def check():
    word = str(input("Enter Word: "))

    with open("practice.txt", "r") as f:
        datas = f.read()
        if (word in datas):
            print("found")
        else:
            print("not found")

check()


#to find in which line
def checkline():
    word = "learning"
    line = 1
    with open("practice.txt", "r") as f:
        while True:
            data = f.readline()
            if (word in data):
                print("found in", line)
            line += 1
    return -1
    
checkline()


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
    def __init__(self, name, balance, account_no):
        self.name = name
        self.balance = float(balance)
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
    
acc = Account("Khelemba", 10000, 19052006)
acc.credit(5000)
acc.debit(2500)