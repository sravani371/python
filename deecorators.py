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

import time
import functools
# Timing decorator
def timer2(delay):
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # start = time.asctime()
            start = time.time()
            print("Started: ", start)
            time.sleep(delay)
            print(f"Sum : {func(*args, **kwargs)}")
            # end = time.asctime().split()
            end = time.time()
            print(f"End : {end}")
            print("Time taken: ",end-start)
        return wrapper
    return timer

@timer2(0)
def add(x,y):
    """ This is a Doc String"""
    su = 0
    for i in range(1, x + y + 1):
        su += i
    return su

add(100000,200000)
print(add.__doc__)
print(time.asctime())
print(list(time.asctime().split()))

def tim(delay=3):
    def dec(fn):
        @functools.wraps(fn)
        def indec(*args, **kwargs):
            print(f"Just adding {delay}sec Delay to start the function")
            print(f"Address inside Decorator : {fn}")
            time.sleep(delay)
            result = fn(*args,**kwargs)
            print("Execution Completed")
            return result
        print(f"Address fn: {fn}")
        print(f"Address indec : {indec}")
        return indec
    return dec

k = int(input("Enter Delay : "))
@tim(3)
def add(a,b,c):
    """ Just adding A DOC"""
    return a+b+c
print(f"Address add : {add}")
print(add(10,15,25))
print(add.__doc__)
del k

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("hello")
        result = func(*args, **kwargs)
        print("welcome")
        return result
    return wrapper
def add(a,b):
    return a+b

add=my_decorator(add)
print(add(10,15))


#level-easy
def my_decorator(func):
    def inner():
        print("function is starting")
    def outer():
        print("function is done")
        return func()
    return inner

@my_decorator
def add(a,b):
    return a+b



