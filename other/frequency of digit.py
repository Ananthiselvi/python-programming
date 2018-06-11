a=int(11)
temp=a
loop=0
while(loop<=9):
  a=temp
  count=0
  while(a!=0):
    rem=a%10
    if(rem==loop):
      count=count+1
    a=a/10
  print(count)
  loop=loop+1
    
