#1.
from sys import displayhook

from methods import Inventory


class Student:
    total = 0

    def __init__(self, name, age, student_class):
        self.name = name
        self.age = age
        self.student_class = student_class
        Student.total += 1

    def __str__(self):
        return f"Name: {self.name}, Class: {self.student_class}, Total: {Student.total}"
    def __repr__(self):
        return self.__str__()

s1 = Student("Nikhil", 16, 10)
s2 = Student("Ram", 14, 9)
s3 = Student("Ganesh", 13, 8)
s4 = Student("Geetha", 12, 7)
s5 = Student("Usha", 11, 6)

print(s1, s2, s3, s4, s5)

l = [s1, s2, s3, s4, s5]
print(l)

#2.
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"position at ({self.x},{self.y})"
    def __repr__(self):
        return self.__str__()
v1 = vector(1, 2)
v2 = vector(2, 3)
print(v1, v2)
l=[v1, v2]
print(l)

#3.
class A:
    def __init__(self, x):
        self.x = x
    def __add__(self,o2):
        return (self.x + o2.x)

a1=A(20)
a2=A(10)

print(a1+a2)

#4.
class inventory:
    def __init__(self):
        self.l = []
    def __add__(self,o2):
        self.l.append(o2)
        return self
    def __str__(self):
        return str(self.l)

i1=inventory()
print(i1+"pencil")

#5.
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self,o2):
        return (self.x + o2.x, self.y + o2.y)
    def __sub__(self,o2):
        return (self.x - o2.x, self.y - o2.y)
    def __div__(self,o2):
        return (self.x / o2.x, self.y / o2.y)
    def __mul__(self,o2):
        return (self.x * o2.x, self.y * o2.y)
    def __mod__(self,o2):
        return (self.x % o2.x, self.y % o2.y)

v1=vector(1, 2)
v2=vector(7, 8)
print(v1+v2)
print(v1-v2)
print(v1%v2)
print(v1*v2)


#7.
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add(self, item):
        self.cart.append(item)

    def __add__(self, other):
        self.cart.append(other)
        return self

    def __repr__(self):
        return f"ShoppingCart({self.cart})"

c1 = ShoppingCart()
c2 = ShoppingCart()

c1.add("hello" "world")
c2.add("world" "hello")
print(c1+c2)

l = [c1, c2]

print(l)
# extrend only add like elements
#eg.
class inventory:
    def __init__(self,l):
        self.Iv = l
    def add(self,item):
        self.Iv.extend(item)
    def __add__(self,o2):
        k=self.Iv+o2.Iv
        return inventory(k)
    def __str__(self):
        return str(self.Iv)
    def __repr__(self):
        return f"inventory({self.Iv})"

i1=inventory([])
i2=inventory([])
i3=inventory([])
i1.add(["kinderjoy"])
i2.add(["maagie"])
i3.add(["yellow"])
I4=i1+i2+i3
print(I4.Iv)


class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self,o2):
        x=self.x + o2.x
        y=self.y + o2.y
        return vector(x,y)
    def __repr__(self):
        return f"vector({self.x},{self.y})"

v1=vector(1, 2)
v2=vector(2, 3)
v3=vector(3, 4)
v4=v1+v2+v3
print(v4)





