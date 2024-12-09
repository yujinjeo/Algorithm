import sys, math

input = sys.stdin.readline

a,b=map(int,input().split(' '))

prime=[]
counts=[0 for _ in range(b+1)]

def is_prime(x):
  end = int(math.sqrt(x))
  if x<=3:
    return True
  for i in range(2,end+1):
    if x%i==0:
      if x//i in prime:
        counts[x]=2
      else:
        counts[x]=1+counts[x//i]
      return False
  return True

for i in range(2,b+1):
  if is_prime(i):
    prime.append(i)
    
answer=0
for i in range(a,b+1):
  if counts[i] in prime:
    answer+=1

print(answer)
  
