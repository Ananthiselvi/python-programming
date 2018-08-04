a=[]
b=int(input('enter the size: '))
for i in range(0,b):
  c=input("enter the number: ")
  a.append(c)
  a.sort()
i=b-1
while(i>-1):
  d=a[i]
  i=i-1
  print(d)
