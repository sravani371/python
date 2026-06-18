def intro(name, city, hobby):
    print(f"{name} lives in {city} and enjoys {hobby}.")

# First order
intro("Ravi", "Hyderabad", "painting")

# Different order
intro("painting", "Ravi", "Hyderabad")

def subtract(a, b):
    return a - b

print(subtract(10, 3))
print(subtract(3, 10))

def greet(name, age):
    print(name, age)

greet("Alice", 20)

def bio(first_name, last_name, age):
    print(f"{first_name} {last_name} is {age} years old.")

# Positional arguments
bio("John", "Doe", 25)
