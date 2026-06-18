c=[10,20,180,40,120,90]
p=sorted(filter(lambda x: 60>x<120,map(lambda x:int((x*9/5)+32),c)),key=lambda x:x%4)
print(p)