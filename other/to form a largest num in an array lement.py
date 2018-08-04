a=[]
b=int(input("enter the number of size: "))
for i in range(0,b):
  c=input("enter the number: ")
  a.append(c)
  a.sort()
d=a[::-1]
e=''.join(d)
print(e)
