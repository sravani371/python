def fun(x,y):
    def fun2(x):
        print(x*y)
    fun2(x)
fun(10,20)

#Sometimes a function is needed only inside another function. Instead of creating it globally, you keep it inside
def greet(name):
    def format_name():
        return name.capitalize()

    print("Hello,", format_name())

greet("chinni")

#A nested function cannot be called directly from outside:
def outer():
    def inner():
        print("Hi")

outer()
