import sys
from collections import deque

input=sys.stdin.readline

n,k=map(int,input().split())
board=[list(map(int, input().split())) for _ in range(n)]
s,r,o=map(int,input().split())

virus=[]

for i in range(n):
  for j in range(n):
    if board[i][j]!=0:
      virus.append((i,j,board[i][j],0))

virus.sort(key=lambda x : x[2])

d=[(0,1),(1,0),(-1,0),(0,-1)]
q=deque(virus)
time=0
while q:
  x,y,v,t=q.popleft()
  if t!=time:
    time+=1
  if time==s:
    break
  for i in range(4):
    dx,dy=d[i]
    a,b=x+dx,y+dy
    if 0<=a<n and 0<=b<n:
      if board[a][b]==0:
        board[a][b]=v
        q.append((a,b,v,t+1))

print(board[r-1][o-1])
