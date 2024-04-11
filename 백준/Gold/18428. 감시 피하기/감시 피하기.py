import sys
from copy import deepcopy

input=sys.stdin.readline

n=int(input())
board=[list(map(str, input().split())) for _ in range(n)]
visited=[[False for _ in range(n)] for _ in range(n)]

teachers=[]
for i in range(n):
  for j in range(n):
    if board[i][j]=='T':
      teachers.append((i,j))
tl=len(teachers)

def mon(can):
  for i in range(tl):
    x,y=teachers[i]
    for j in range(x,n):
      if can[j][y]=='O':
        break
      elif can[j][y]=='S':
        return 
    for j in range(x,-1,-1):
      if can[j][y]=='O':
        break
      elif can[j][y]=='S':
        return
    for j in range(y,n):
      if can[x][j]=='O':
        break
      elif can[x][j]=='S':
        return
    for j in range(y,-1,-1):
      if can[x][j]=='O':
        break
      elif can[x][j]=='S':
        return 
  return 'YES'

def bact(lst,cnt):
  if cnt==3:
    can=deepcopy(board)
    for i in range(3):
      x,y=lst[i]
      can[x][y]='O'
    rst=mon(can)
    if rst=='YES':
      global answer
      answer=rst
    return
      
  for i in range(n):
    for j in range(n):
      if board[i][j]=='X' and (i,j) not in lst:
        lst.append((i,j))
        bact(lst,cnt+1)
        lst.remove((i,j))


answer='NO'        
lst=[]
bact(lst,0)
print(answer)