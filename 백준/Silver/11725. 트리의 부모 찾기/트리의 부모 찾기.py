import sys
from collections import deque

n=int(input())
ans=[0 for _ in range(n+1)]
ans[1]=-1
board=[[] for _ in range(n+1)]

for i in range(n-1):
  x,y=map(int,sys.stdin.readline().split())
  board[x].append(y)
  board[y].append(x)

def bfs():
  q=deque()
  q.append(1)
  while q:
    t=q.popleft()
    for u in board[t]:
      if ans[u]==0:
        ans[u]=t
        q.append(u)

bfs()

for i in range(2,n+1):
  print(ans[i])