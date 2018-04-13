a=[]
b=int(input("enter the size of the list: "))
for i in range(b):
    c=int(input("enter the number: "))
    a.append(c)
    a.sort()
t=len(a)
q=t//2
if(t%2!=0):
    y=(q+1)
    p=a[y-1:y]
    print(p)
else:
    e=a[q-1:q+1]
    f=(sum(e)/2)
    print(f)
    
