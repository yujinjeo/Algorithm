import sys
from copy import deepcopy

input = sys.stdin.readline

n=int(input())
board=[list(map(str,input().rstrip().split(' ')))for _ in range(n)]

teachers=[]

for i in range(n):
  for j in range(n):
    if board[i][j]=='T':
      teachers.append((i,j))

d=[(0,1),(1,0),(-1,0),(0,-1)]

def is_detected(cand):
  
  for x,y in teachers:
    for dx,dy in d:
      a=x+dx
      b=y+dy
      while True:
        if 0<=a<n and 0<=b<n and (cand[a][b]=='S' or cand[a][b]=='X'):
          if cand[a][b]=='S':
            return False
          
          a+=dx
          b+=dy
        else:
          break
  return True

answer='NO'

def bact(r,c,lst,cnt):
  global answer
  if cnt==3:
    cand=deepcopy(board)
    for x,y in lst:
      cand[x][y]='O'
    val=is_detected(cand)
    if val:
      answer='YES'
    return
  for i in range(r,n):
    c=r if i==r else 0
    for j in range(c,n):
      if board[i][j]=='X' and (i,j) not in lst:
        lst.append((i,j))
        bact(i,j,lst,cnt+1)
        lst.remove((i,j))


bact(0,0,[],0)

print(answer)
          
      
      

