#Day 2: 30 days of programming
first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
full_name = first_name + last_name
print(full_name)
country = str(input("Enter country: "))
city = str(input("Enter city: "))
age = int(input("Enter your age: "))
year = int(input("Enter the year: "))
is_married = False
is_true = str(input("Are you married: y/n"))
if (is_true == "y"):
    is_married = True
else:
    is_married = False

is_light_on = False

anime, movie, show = "Darling in Franxx", "Suzume", "The Ultimate Spider-Man"

#Level 2
print(type(first_name))
print(type(last_name))
print(len(first_name))
print(len(last_name))
if len(first_name) < len(last_name):
    print("Length of last name is bigger")
else:
    print("Length of first name is bigger")

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_two / num_one
remainder = num_two % num_one
exp = num_one**num_two


radius = 30
pie = 22/7
def area():
    return pie*radius**2
def circumference():
    return 2*pie*radius