import sys
import copy

input=sys.stdin.readline

n=int(input())
board=[list(input().strip().split()) for _ in range(n)]
answer='NO'
teachers=[]
for i in range(n):
  for j in range(n):
    if board[i][j]=='T':
      teachers.append((i,j))


def makeObj(cnt):
  global answer
  if cnt==3:
    if spread():
      answer='YES'
    return
  for i in range(n):
    for j in range(n):
      if board[i][j]=='X':
        board[i][j]='O'
        makeObj(cnt+1)
        board[i][j]='X'
        
d=[(0,1),(0,-1),(1,0),(-1,0)]

def spread():
  tmp=copy.deepcopy(board)
  for i in range(len(teachers)):
    x,y=teachers[i]
    for i in range(4):
      dx,dy=d[i]
      a,b=x+dx,y+dy
      while 0<=a<n and 0<=b<n:
        if tmp[a][b]=='X':
          tmp[a][b]='T'
        elif tmp[a][b]=='S':
          return False
        elif tmp[a][b]=='O':
          break
        a+=dx
        b+=dy
  return True

makeObj(0)
print(answer)