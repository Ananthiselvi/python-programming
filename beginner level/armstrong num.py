a=int(input("enter the number: "))
b=len(str(a))
sum = 0
temp = a
while a> 0:
   digit = a % 10
   sum += digit ** b
   a//= 10
if temp== sum:
    print("Armstrong number")
else:
    print("not an Armstrong number")
