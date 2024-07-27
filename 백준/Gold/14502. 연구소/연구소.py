import sys
from copy import deepcopy
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())

virus=[]
board=[]

for i in range(n):
  lst=list(map(int, input().split(' ')))
  board.append(lst)
  for j in range(len(lst)):
    if lst[j]==2:
      virus.append((i,j))

d=[(0,1),(1,0),(-1,0),(0,-1)]

def spread(lab):
  q=deque(virus)
  while q:
    x,y=q.popleft()
    for dx,dy in d:
      a=x+dx
      b=y+dy
      if 0<=a<n and 0<=b<m and lab[a][b]==0:
        lab[a][b]=2
        q.append((a,b))
  k=0
  for i in range(n):
    for j in range(m):
      if lab[i][j]==0:
        k+=1
  
  return k

answer=0
def bact(x,y,lst,cnt):
  global answer
  if cnt==3:
    lab=deepcopy(board)
    for i,j in lst:
      lab[i][j]=1
    answer=max(answer,spread(lab))
    return
  for i in range(x,n):
    start_j=y if x==i else 0
    for j in range(start_j,m):
      if board[i][j]==0:
        lst.append((i,j))
        bact(i,j+1,lst,cnt+1)
        lst.remove((i,j))

bact(0,0,[],0)
print(answer)

