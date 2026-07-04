a=[1,2,3,4]
b=[10,20,30,40,50]
num=list(map(lambda a,b:a+b,a,b))
print(num)

a=[12,15,7,18,20,21,25]
nums=list(filter(lambda a:a%3 or a%5 and not a%3 and a%5,a))
print(nums)

nums=[[1,2],[3,4],[5,6]]
result=list(map(lambda x: x.append(10),nums))
print(result)

data = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda sub: list(map(lambda x: x + 5, sub)), data))
print(result) # Output: [[6, 7], [8, 9], [10, 11]]

d = {"apple": 100, "banana": 40, "cherry": 150}
result = list(filter(lambda x: d[x]>50,d))
print(result)

from functools import reduce
d=[10,20,40,34]
result=reduce(lambda x,y: a if  a>b else b,d)
print(result)

from functools import reduce
d={"hello"}
result=reduce(lambda x,:x,d)
print(result)

num=['P', 'y', 't', 'h', 'o', 'n']
l=reduce(lambda x,y:x+y,num)
print(l)

st="chinni"
s=list(filter(lambda x:x not in "aeiouAEIOU",st))
print("".join(s))

st="chinni"
s=list(map(lambda x:x not in "aeiouAEIOU",st))
print(s)

st="chinni"
s=reduce(lambda x,y:x+y,st)
print(s)

l=[2,3,5,7,8,9]
s=list(sorted(l,key=lambda x:x//3))
print(s)

s="hello"
s=reduce(lambda x,y:x+"@"+y,s)
print(s)

l=[1,2,3,4,5,6]
s=reduce(lambda x,y:x*y,l)
print(s)

def register(age,name="Alice", country="india"):
    return age,name,country
print(register(21))












