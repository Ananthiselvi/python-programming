n=int(input("enter the number: "))
a=[]
b=int(input("enter the size of the element: "))
for i in range(1,b+1):
    c=input("enter the number: ")
    a.append(c)
a.sort()
print(a[n-1])
