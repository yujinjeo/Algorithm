import sys
input=sys.stdin.readline

n,m=map(int,input().split())

x,y,d=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]

move={0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
board[x][y]=2
answer=1

def turn_left():
  global d
  d=(d-1)%4

while True:
  flag=0
  for i in range(4):
    turn_left()
    dx,dy=move[d]
    a=dx+x
    b=dy+y
    if 0<=a<n and 0<=b<m:
      if board[a][b]==0:
        x,y=a,b
        board[a][b]=2
        answer+=1
        flag=1
        break
  if flag==1:
    continue
  dx,dy=move[d]
  a=-dx+x
  b=-dy+y
  if 0<=a<n and 0<=b<m:
    if board[a][b]!=1:
      x,y=a,b
      continue
    else:
      break

print(answer)
      
