def dec(func):
    def inner():
        print("starting from functions")
        print(func.__name__)
        func()
        print("ending from functions")
    return inner
@dec
def greet():
    print("hello world")
greet()


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
def greet():
    print("hello world")
greet()

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper
def add(a, b):
    return a+b
add=my_decorator(add)
print(add(3, 4))

def vaild(func):
    us = ["sravani","sravika","chinni"]
    special_char = ['@',"!","#","$","%","^","&","*"]
    def inner(us,psd:str):
        if 8 <= len(psd) <= 15:
            k = list(filter(lambda x: x in special_char, psd))
            n = list(filter(lambda x: x.isdigit(), psd))
            up = list(filter(lambda x: x.isupper(), psd))
            print(k)
            print(n)
            print(up)

            if up and n and k:
                return func(us,psd)
            else:
                return "Invalid Password"
        else:
            return "Minimum length of the password is 8 characters"
    return inner


@vaild
def register(username,password):
    return f"{username}'s Register Successful"

print(register("sravani","chinni@9063"))

def Upper(x):
    for i in x:
        if i.isupper():
            return True
    return False

def vaild(func):
    uns = []
    special_char = ['@',"!","#","$","%","^","&","*"]
    def inner(us:str,psd:str,age:int):
        nonlocal uns
        if us not in uns:
            uns.append(us)
            if 8 <= len(psd) <= 15:
                k = list(filter(lambda x: x in special_char, psd))
                n = psd.isalnum()
                up = Upper(psd)
                # print(k)
                # print(n)
                # print(up)

                if up and n and k:
                    if age >= 18:
                        return func(us,psd,age)
                    else:
                        return "Age must be greater than 17"
                else:
                    return "Invalid Password"
            else:
                return "Minimum length of the password is 8 characters"
        else:
            return "Username already exists"
    return inner


@vaild
def register(username,password,age):
    return f"{username}'s Register Successful"

print(register("sravani","chinni143$$",19))
print(register("sravani","chinni143$$",19))





