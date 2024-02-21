n=int(input())

lst=["" for _ in range(1001)]

lst[1]="SK"
lst[2]="CY"
lst[3]="SK"

if n<=3:
  print(lst[n])
else:
  for i in range(4,n+1):
    if lst[i-1]=="SK" and lst[i-3]=="SK":
      lst[i]="CY"
    else:
      lst[i]="SK"
  print(lst[n])