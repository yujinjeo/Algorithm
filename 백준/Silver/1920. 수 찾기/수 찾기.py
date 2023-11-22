import sys

n=int(input())
a=list(map(int, sys.stdin.readline().split()))
m=int(input())
list=list(map(int, sys.stdin.readline().split()))

ans=[0]*m
a=sorted(a)

def bs(start,end,q):
  if start>end:
    return 0 
  mid=int((start+end)/2)
  if q==a[mid]:
    return 1
  elif q<a[mid]:
    return bs(start,mid-1,q)
  else:
    return bs(mid+1, end,q)
  
for i in range(m):
  ans[i]=bs(0,n-1,list[i])

for a in ans:
  print(a)