a=int(input("enter the number: "))
c=a%10
z=c*c
b=a//10
while(b>c):
  e=b//10
  e=e*e
  f=b%10
  f=f*f
  b=e+f
j=b+z
print(j)
