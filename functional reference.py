count = len

numbers = [10, 20, 30, 40, 50]

print(count(numbers))

#2
def run_twice(func, value):
    return func(func(value))

# Example function
def double(x):
    return x * 2

result = run_twice(double, 5)
print(result)

#3
operations = {
    "upper": str.upper,
    "lower": str.lower,
    "title": str.title
}

choice = input("Choose (upper/lower/title): ")

text = input("Enter text: ")

if choice in operations:
    print(operations[choice](text))
else:
    print("Invalid choice")

#4
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)

print(times3(5))
print(times3(10))

#5
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)

print(times3(5))
print(times3(10))