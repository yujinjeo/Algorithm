import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

board=[list(map(int,list(map(str,sys.stdin.readline().strip())))) for _ in range(n)]

d=[(-1,0),(1,0),(0,1),(0,-1)]

def bfs():
  q=deque()
  q.append((0,0))
  while q:
    i,j=q.popleft()
    for dx,dy in d:
      x=i+dx
      y=j+dy
      if 0<=x<n and 0<=y<m:
        if board[x][y]==1:
          q.append((x,y))
          board[x][y]=board[i][j]+1

bfs()

print(board[n-1][m-1])