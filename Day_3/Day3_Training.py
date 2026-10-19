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
