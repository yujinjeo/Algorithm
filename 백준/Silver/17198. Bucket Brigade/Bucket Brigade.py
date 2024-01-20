import sys
from collections import deque

farm=[list(map(str,sys.stdin.readline().strip())) for _ in range(10)]

d=[(0,1),(0,-1),(1,0),(-1,0)]

def bfs(r,w):
  q=deque()
  q.append((r,w))
  farm[r][w]=0

  while q:
    i,j=q.popleft()
    for dx, dy in d:
      x=i+dx
      y=j+dy
      if 0<=x<10 and 0<=y<10:
        if farm[x][y]=='L':
          return farm[i][j]
        if farm[x][y]=='.':
          q.append((x,y))
          farm[x][y]=farm[i][j]+1

cnt=0
for i in range(10):
  for j in range(10):
    if farm[i][j]=='B':
      cnt=bfs(i,j)

print(cnt)