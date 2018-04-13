a=int(input("enter the number: "))
z=a
b=0
while(a>0):
    a=a//10
    b+=1
print(b)
c=z%10
d=c*c
g=0
while(b>1):
    z=z//10
    e=z%10
    f=e*e
    g=g+f
    b-=1
r=g+d
print(r)

