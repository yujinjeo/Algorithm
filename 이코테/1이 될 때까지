import sys
input=sys.stdin.readline

n,k=map(int,input().split())
answer=0

##### 내 풀이
while True:
  if n==1:
    break
  if n%k==0:
    n/=k
  else:
    n-=1
  answer+=1

print(answer)

##### 이코테 풀이

while n>=k:
  while n%k!=0:
    n-=1
    answer+=1
  n/=k
  answer+=1

while n!=1:
  n-=1
  answer+=1

print(answer)
    
