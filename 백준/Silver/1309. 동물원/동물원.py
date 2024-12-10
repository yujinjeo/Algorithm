n=int(input())

if n==1:
  print(3)
elif n==2:
  print(7)
else:
  a,b=2,3

  for i in range(2,n):
    x=a+b
    y=a*2+b
    a,b=x,y

  print((a*2+b)%9901)
  