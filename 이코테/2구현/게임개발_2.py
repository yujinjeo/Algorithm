import sys

input=sys.stdin.readline

n,m=map(int,input().split())

x,y,d=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]

# 0 1 2 3 
direction=[(-1,0),(0,-1),(1,0),(0,1)]
board[x][y]=2

cnt=1
while True:
  back=True
  for _ in range(4):
    dx,dy=direction[d]
    if 0<=dx+x<n and 0<=dy+y<m and board[dx+x][dy+y]==0:
      x+=dx
      y+=dy
      board[x][y]=2
      cnt+=1
      back=False
      break
    else:
      d=(d+1)%4
  if back:
    dx,dy=direction[d]
    if 0<=x-dx<n and 0<=y-dy<m and board[x-dx][y-dy]!=1:
      x-=dx
      y-=dy
    else:
      break

print(board)
print(cnt)      
    

# while True:
  
