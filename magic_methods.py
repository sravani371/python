#1.
from sys import displayhook


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

#6.
class A:
    def __init__(self, x):
        self.x = x
        self.y = y
        A.display(self)

    def display(self):
        return (self.x, self.y)

a1 = A(1, 2)
a2 = A(7, 8)

a1.display()
a2,display()




