u=1
q=0
lst=[0 for _ in range(10001)]

def d(n):
  ans=n
  k1=n//1000
  k2=(n//100)%10
  k3=(n//10)%10
  k4=n%10
  ans+=k1+k2+k3+k4
  return ans

while True:
  q=d(u)  
  if u<=10000:
    if q<=10000:
      lst[q]+=1
      u+=1
    else:
      u+=1
      continue
  else:
    break

for i in range(1, 10000):
  if lst[i]==0:
    print(i)

