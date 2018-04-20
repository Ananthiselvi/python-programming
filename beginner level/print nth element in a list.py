a=[]
b=int(input("enter the size: "))
d=int(input("enter the nth number: "))
for i in range(b):
  c=input("enter the number: ")
  a.append(c)
  a.sort()
print(a[d-1:d])
