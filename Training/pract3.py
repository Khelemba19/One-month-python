import math
import os

age = int(20)
ur_height = float(164)
x1y1 = 4+2j


#entering base and height of a triangle and calculating their area
base = float(input("Enter Base: "))
height = float(input("Enter the height of the triangle: "))

area_triangle = 0.5*base*height
print(area_triangle)


#sides of a triangle and calculating their perimeter

a = float(input("Enter sides a: "))
b = float(input("Enter sides b: "))
c = float(input("Enter sides c: "))

perimeter = a + b + c
print(perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

len1 = float(input("Enter length of the rectangle: "))
widt = float(input("Enter width of the rectangle: "))

area_rectangle = len1 * widt
perimeter_rectangle = 2 * (len1 + widt)

print("Area of the rectangle", area_rectangle)
print("Perimeter of the rectangle", perimeter_rectangle)


#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

rad = int(input("Enter radius of the circle: "))
pi = 3.14
area_of_circle = pi * rad **2
circumference_circle = 2 * pi * rad

print("Area of circle: ", area_of_circle)
print("Circumference of the circle", circumference_circle)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

slope1 = 2
y_intercept = -2

x_intercept = -y_intercept / slope1

print("Slope is: ", slope1)
print("Y-intercept is: ", y_intercept)
print("X-intercept is: ", x_intercept)


#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1, y1 = 2, 2
x2, y2 = 6, 10

slope2 = (y2 - y1)/ (x2 - x1)

dis = ((x2-x1)**2 + (y2-y1)**2) ** 0.5

print("Slope is: ", slope2)
print("Euclidean distance is: ", dis)


#comparint two slope
import math

if math.isclose(slope1, slope2):
    print("The two slopes are parallel")
elif math.isclose(slope1, slope2, -1):
    print("The two slopes are perpendicular")
else:
    print("The two slopes intersect at an angle")

#checking and slicing
ex = "I hope this code is not full of jargon"
is_present = "jargon" in ex
print(ex.find("jargon"))
print(is_present)

tex = "python"
print(len(tex))
val = float(len(tex))
print(type(val))
val = str(val)
print(type(val))


#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

even_odd = int(input("Enter numbers: "))
if  even_odd%2 == 0:
    print(even_odd, "Its even")
else:
    print("Not even")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
val2 = int(2.7)
div = 7//3
if (val2 == div):
    print("Is equal")
else:
    print("not equal")


#checking between variables and interger
type1 = "10"
type2 = 10
if type(type1) == (type2):
    print("'10' and 10 are same in python")
else:
    print("'10' and 10 are not same in python")


type3 = int(float("9.8"))
type4 = 10
if type3 == type4:
    print("'9.8' and 10 are same")
else:
    print("'9.8' and 10 are not the same")


#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter weekly working hours: "))
rate = float(input("Enter rate per hour"))
pay = hours * rate
print(pay)

#to calculate how many years is in a year

years = 100
seconds = 60 * 60 * 24 * 365
print(years * seconds)

#question 23, to makes a table with numbers

for i in range(1, 6):
    print(f"{i}, 1, {i}, {i**2}, {i**3}")


#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = ['Thirty', 'Days', 'Of', 'Python']
new_str1 = " ".join(str1)
print(new_str1)


#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str2 = "Coding"
str3 = "For"
str4 = "All"
new_str2 = str2 + " " + str3 + " " + str4
print(new_str2)


#Declare a variable named company and assign it to an initial value "Coding For All".Print the variable company using print(). Print the length of the company string using len() method and print(). Change all the characters to uppercase letters using upper() method. Change all the characters to lowercase letters using lower() method.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All. Cut(slice) out the first word of Coding For All string. Check if Coding For All string contains a word Coding using the method index, find or other methods.Replace the word coding in the string 'Coding For All' to Python.Change "Python for Everyone" to "Python for All" using the replace method or other methods.Split the string 'Coding For All' using space as the separator (split()). "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma. What is the character at index 0 in the string Coding For All. What is the last index of the string Coding For All. What character is at index 10 in "Coding For All" string. Create an acronym or an abbreviation for the name 'Python For Everyone'. Create an acronym or an abbreviation for the name 'Coding For All'. Use index to determine the position of the first occurrence of C in Coding For All.Use index to determine the position of the first occurrence of F in Coding For All. Use rfind to determine the position of the last occurrence of l in Coding For All People. 

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0: 6])
print("The word 'Coding' is in index: ",company.find("Coding"))
print(company.startswith("Coding"))
new_company = company.replace("Coding", "Python")
company2 = "Python for Everyone"
print(company2.replace("Everyone", "All"))
print(company.split())
company3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company3.split(", "))
print("The first character at the string 'Coding for All' is: ", company[0])
print("The 10th character at the string 'Coding for All' is: ", company[9])
py4e = "Python For Everyone"
c4a = "Coding For All"
print(c4a.find("C"))
print(c4a.find("F"))
print(c4a.rfind("l"))


#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

word = "You cannot end a sentence with because because because is a conjunction"
print(word.find("because"))
print(word.index("because"))
print(word.rfind("because"))
print(word.rindex("because"))
slice_word = word[31:54]
print(slice_word)


#Does 'Coding For All' start with a substring Coding?
#Does 'Coding For All' end with a substring coding?
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

print(company.startswith("Coding"))
print(company.endswith("coding"))

company4 = '   Coding For All      '
print(company.strip())

var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())


#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
company5 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
new_company5 = "# ".join(company5)
print(new_company5)

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\ Age\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {}".format(a, b, a*b))
print("{} % {} = {}".format(a, b, a%b))
print("{} // {} = {}".format(a, b, a//b))
print("{} ** {} = {}".format(a, b, a**b))