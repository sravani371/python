x = "hello"
x = x + " world"  # A NEW string object is created; "hello" still exists in memory
print(x)           # hello world

my_list = [1, 2, 3]
my_list.append(4)  # Modified IN PLACE — same object, no copy
print(my_list)     # [1, 2, 3, 4]



fruits = ['apple', 'banana', 'cherry']
fruits.append('date')     # ['apple', 'banana', 'cherry', 'date']
fruits[1] = 'blueberry'   # Modify in place
print(len(fruits))


name = "Python"
print(name[0])       # P  — indexing
print(name[1:4])     # yth  — slicing
print(name.upper())  # PYTHON

#list
fruits = ['apple','banana','cherry']
#fruits.append('date')     # ['apple', 'banana', 'cherry', 'date']
fruits[1] = 'blueberry'   # Modify in place
print(len(fruits))

point = (10, 20)
x, y = point             # Tuple unpacking
print(x) 