#Idk just practicing
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c = Circle(10)
print(c.area())
print(c.perimeter())        


#Company class
class Employee:
    def __init__(self, department, role, salary):
        self.department = department
        self.role = role
        self.salary = salary

    def show(self):
        print("Department = ", self.department) 
        print("Role = ", self.role) 
        print("Salary = Rs.", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("IT", "Dev", "60,000")
        print("Name = ", self.name)
        print("Age = ", self.age)

Em1 = Employee("Human Resource", "Inspector", "20,000")
Em1.show()
Eng1 = Engineer("Rando", 20)
Eng1.show()



class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, od2):
        return self.price > od2.price
            
od1 = Order("Brush", 30)
print(od1.item, end= ", ")
print(od1.price)
od2 = Order("Pen", 50)
print("Is", od1.price, ">", od2.price, od1 > od2)