def dec(func):
    def inner(n):
        print("starting from functions")
        print(func.__name__)
        func(n)
        print("ending from functions")
    return inner
@dec
def greet(name):
    print(f"hello {name}")
greet("sravani")

def login(func):
    def inner():
        un=input("Enter your username: ")
        psd=input("Enter your password: ")
        if un=="dharavath" and psd=="sra":
            return func()
        else:
            return "Invalid credentials"
    return inner
@login
def securefile():
    return "Secret File"
print(securefile())

def greet(func):
    def wrapper():
        print("starting from functions")
        print(func.__name__)
        func()
        print("ending from functions")
    return wrapper
@greet
def greet(name):
    print("hello world")
greet("name")



