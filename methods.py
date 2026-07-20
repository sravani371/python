class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40

student1 = Student("Alice", 75)
student2 = Student("Bob", 35)

for student in [student1, student2]:
    if student.is_passed():
        print(f"{student.name} has passed.")
    else:
        print(f"{student.name} has failed.")

# 2.employee
class Employee:
    company_name = "TechCorp"   # Class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


emp1 = Employee("Alice")
emp2 = Employee("Bob")

print("Before changing company:")
print(emp1.name, "-", emp1.company_name)
print(emp2.name, "-", emp2.company_name)

Employee.change_company("InnovateTech")

print("\nAfter changing company:")
print(emp1.name, "-", emp1.company_name)
print(emp2.name, "-", emp2.company_name)

#3.
class MathOps:

    @staticmethod
    def is_even(num):
        return num % 2 == 0


# Call using class
print(MathOps.is_even(10))

# Create object
obj = MathOps()

# Call using instance
print(obj.is_even(7))


#4.
class Car:
    wheels = 4

    def __init__(self, mileage):
        self.mileage = mileage   # Instance attribute

    def display_specs(self):
        print("Mileage:", self.mileage)
        print("Wheels:", Car.wheels)

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels


car1 = Car(20)
car2 = Car(25)

print("Before changing wheels:")
car1.display_specs()
print()
car2.display_specs()

Car.change_wheels(6)

print("\nAfter changing wheels:")
car1.display_specs()
print()
car2.display_specs()

#5
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def show_conversion(self):
        print("Temperature in Celsius:", self.celsius, "°C")
        print("Temperature in Fahrenheit:", Temperature.to_fahrenheit(self.celsius), "°F")


t1 = Temperature(30)
t1.show_conversion()


#7
class Product:
    # Class attribute
    tax_rate = 10  # 10%

    # Constructor
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    # Instance method
    def final_price(self):
        tax = (self.base_price * Product.tax_rate) / 100
        return self.base_price + tax

    # Class method
    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    # Static method
    @staticmethod
    def is_valid_price(price):
        return price >= 0 and price <= 1000000


# Creating multiple products
product1 = Product("Laptop", 50000)
product2 = Product("Mobile", 20000)
product3 = Product("Headphones", -500)

print("Initial Tax Rate:", Product.tax_rate, "%")

print("\nProduct Prices:")
print(product1.name, "Final Price =", product1.final_price())
print(product2.name, "Final Price =", product2.final_price())

# Validity Check
print("\nPrice Validity:")
print(product1.name, ":", Product.is_valid_price(product1.base_price))
print(product2.name, ":", Product.is_valid_price(product2.base_price))
print(product3.name, ":", Product.is_valid_price(product3.base_price))

# Change tax rate
Product.change_tax_rate(18)

print("\nUpdated Tax Rate:", Product.tax_rate, "%")

print("\nUpdated Product Prices:")
print(product1.name, "Final Price =", product1.final_price())
print(product2.name, "Final Price =", product2.final_price())

#8.
class Inventory:
    # Class attributes
    total_items = 0
    threshold = 20

    def __init__(self):
        # Instance attribute
        self.stock = {}

    def add(self, item, qty):
        if Inventory.valid(qty):
            self.stock[item] = qty
            print("Item added successfully")
            Inventory.total_items += 1
        else:
            print("Quantity should reach minimum threshold")

    @staticmethod
    def valid(q):
        return q >= Inventory.threshold

    def remove(self, item):
        if item in self.stock:
            self.stock.pop(item)
            print(f"{item} removed from inventory")
            Inventory.total_items -= 1
        else:
            print("Item not found")

#9.
class Course:
    total = 0
    min_duration = 3

    def __init__(self, title, dur, est):
        self.title = title
        self.duration = duration
        self.enrolled_student = est
        Course.total += 1

    def enroll(self, n):
        self.enrolled_student += n

    @classmethod
    def update(cls, nd):
        cls.min_duration = nd
        print("minimum duration updates")

    @staticmethod
    def valid(d):
        return d >= 3






