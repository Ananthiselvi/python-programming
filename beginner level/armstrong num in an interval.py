a=int(input("enter the number: "))
b=int(input("enter the number: "))
for i in range(a,b+1):
    c=len(str(i))
    sum = 0
    temp = i
    while i> 0:
       digit = i % 10
       sum += digit ** c
       i//= 10       
    if temp== sum:
        print(temp)
        
