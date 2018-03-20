a=int(input("enter the number: "))
b=int(input("enter the number: "))
for c in range(a,b):
    if(c>1):
        for i in range(2,c):
            if(c%i==0):
                break
        else:
             print(c)
