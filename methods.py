# 1.student
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


# Create object
t1 = Temperature(30)

# Show conversion
t1.show_conversion()


