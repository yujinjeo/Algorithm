import sys
from collections import deque

input = sys.stdin.readline

n=int(input())

board=[[0 for _ in range(n)] for _ in range(n)]
appletimes=int(input())
for _ in range(appletimes):
  a,b=map(int,input().split(' '))
  board[a-1][b-1]=1

turntimes=int(input())
time=[]
turn=[]

for _ in range(turntimes):
  a,b=map(str,input().rstrip().split(' '))
  time.append(int(a))
  turn.append(b)

# 동 남 서 북 시계방향으로
move=[(1,0),(0,-1),(-1,0),(0,1)]

direction=0

def turnfnc(c):
  global direction
  if c=='D':
    direction=(direction+1)%4
  else:
    direction=(direction-1)%4
    

queue=deque()
queue.append((0,0))
board[0][0]=2
t=0
turnindex=0
while True:
  if turnindex<turntimes and t==time[turnindex]:
    turnfnc(turn[turnindex])
    turnindex+=1
  x,y=queue[-1][0],queue[-1][1]
  if 0<=x+move[(direction-1)%4][0]<n and 0<=y+move[(direction-1)%4][1]<n and board[x+move[(direction-1)%4][0]][y+move[(direction-1)%4][1]]!=2:
    x+=move[(direction-1)%4][0]
    y+=move[(direction-1)%4][1]
    if board[x][y]==0:
      queue.append((x,y))
      board[x][y]=2
      lx,ly=queue.popleft()
      board[lx][ly]=0
    else:
      queue.append((x,y))
      board[x][y]=2    
  else:
    break
  t+=1

print(t+1)
    
    

