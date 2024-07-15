import sys

input=sys.stdin.readline

n,k=map(int,input().split())

# my sol
# cnt=0
# while n>1:
#   if n%k==0:
#     n//=k
#   else:
#     n-=1
#   cnt+=1

# print(cnt)

# books sol
cnt=0
while True:
  target=(n//k)*k
  cnt+=n-target
  n=target
  if n<k:
    break
  cnt+=1
  n//=k

cnt+=(n-1)
  
