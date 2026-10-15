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