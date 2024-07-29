import sys
from collections import deque

input = sys.stdin.readline
n,m=map(int,input().split(' '))
board=[list(map(int,input().split(' '))) for _ in range(n)]

virus=[]
for i in range(n):
  for j in range(n):
    if board[i][j]!=0:
      virus.append((i,j,board[i][j],0))
virus=sorted(virus,key=lambda x:x[2])

time,x,y=map(int,input().split(' '))

d=[(0,1),(1,0),(-1,0),(0,-1)]

def bfs():
  q=deque(virus)
  while q:
    i,j,v,t=q.popleft()
    if t==time:
      break
    for dx,dy in d:
      a=i+dx
      b=j+dy
      if 0<=a<n and 0<=b<n and board[a][b]==0:
        board[a][b]=v
        q.append((a,b,v,t+1))


bfs()
print(board[x-1][y-1])
