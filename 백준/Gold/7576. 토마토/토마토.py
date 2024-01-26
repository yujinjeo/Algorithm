import sys
from collections import deque

m,n=map(int, sys.stdin.readline().split())

board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

q=deque()
d=[(-1,0),(1,0),(0,1),(0,-1)]

def bfs(q):
  ans=0
  while q:
    i,j=q.popleft()
    ans=board[i][j]
    for dx,dy in d:
      x=i+dx
      y=j+dy
      if 0<=x<n and 0<=y<m:
        if board[x][y]==0:
          board[x][y]=board[i][j]+1
          ans=board[x][y]
          q.append((x,y))
          
  for i in range(n):
    for j in range(m):
      if board[i][j]==0:
        return -1
  if ans==1:
    return 0
  else:
    return ans-1

for i in range(n):
  for j in range(m):
    if board[i][j]==1:
      q.append((i,j))

#처음부터 토마토가 모두 익어있는 상황
ans=bfs(q)
print(ans)