import sys
from collections import deque

A,K=map(int, sys.stdin.readline().split())
lst=[0 for _ in range(K+1)]

def bfs():
  q=deque()
  q.append(A)

  while q:
    i=q.popleft()

    if i==K:
      return lst[K]
      
    if i+1<=K and lst[i+1]==0:
      lst[i+1]=lst[i]+1
      q.append(i+1)
      
    if i*2<=K and lst[i*2]==0:
      lst[i*2]=lst[i]+1
      q.append(i*2)
   

ans=bfs()

print(ans)