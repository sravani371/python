def greet():
    print("Hello World!")
greet()

#the return statement
def add(a, b):
    return a + b


def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")


student_info("Alice", 20, "A")
# Name: Alice, Age: 20, Grade: A

def multiply(a, b, c):
    return a * b * c

# Example
print(multiply(2, 3, 4))

def describe_pet(animal, name):
    print(f"My {animal} is named {name}.")

# Example
describe_pet("dog", "Buddy")

#funtion to calcuate power
def power(base, exponent):
    return base ** exponent

# Example
print(power(2, 3))

#Function to return a full name
def full_name(first, middle, last):
    return f"{first} {middle} {last}"

# Example
print(full_name("John", "Michael", "Doe"))


