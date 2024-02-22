def koong():
  for i in range(k+1):
    if i<2:
      lst[i]=1
    elif i==2:
      lst[i]=2
    elif i==3:
      lst[i]=4
    else:
      lst[i]=lst[i-1]+lst[i-2]+lst[i-3]+lst[i-4]   

n=int(input())
case=[]

for _ in range(n):
  case.append(int(input()))

k=max(case)
lst=[0 for _ in range(k+1)]

koong()

for i in range(n):
  print(lst[case[i]])