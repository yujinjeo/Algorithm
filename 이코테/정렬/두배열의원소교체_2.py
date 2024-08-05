import sys

input = sys.stdin.readline

n,k=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a=sorted(a,key=lambda x:x)
b=sorted(b,key=lambda x:x, reverse=True)

for i in range(k):
  if a[i]<b[i]:
    a[i]=b[i]
  else:
    break

print(sum(a))
