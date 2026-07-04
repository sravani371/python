point = (10, 20)
x, y = point
print(x)

#if condition
a=10
if(a%2==0):
    print("odd")
else:
    print("even")

    #lambda
x=lambda a,b:a+b(10,20)
l=lambda k:k**k
a=l(2)
print(a)

m=lambda x,y,z:(x+y)*2
print(m(10,2,3))

s=lambda x:print(x*5)
print(s(20))

def s(x):
    print(x*5)
    return
print(s(10))


x=10
y=20
print(x if x>y else y)

s=lambda x:x not in "AEIOU aeiou"
print (s('a'))

d=lambda a,b: a if a<b else b
print (d(10,20))


k=input()
for i in k:
   if s(i):
       print(i)
