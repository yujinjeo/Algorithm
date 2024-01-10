import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split())
dq=deque([i for i in range(1,n+1)])
lst=list(map(int,sys.stdin.readline().split()))
cnt=0
for k in lst:
  while (4):
    if dq[0]==k:
      dq.popleft()
      break
    elif dq.index(k)<=len(dq)/2:
      cnt+=dq.index(k)
      dq.rotate(-dq.index(k))
    elif dq.index(k)>len(dq)/2:
      cnt+=len(dq)-dq.index(k)
      dq.rotate(len(dq)-dq.index(k))

print(cnt)