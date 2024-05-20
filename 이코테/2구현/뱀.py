import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
board=[[0 for _ in range(n)] for _ in range(n)]
k=int(input())
apple=[]
for i in range(k):
  x,y=map(int,input().split())
  board[x-1][y-1]=1

l=int(input())
time_list=[]
direction_list=[]
for i in range(l):
  a,b=map(str,input().strip().split())
  time_list.append(int(a))
  direction_list.append(b)

#시계방향으로 북, 동, 남 ,서 
moved=[(-1,0),(0,1),(1,0),(0,-1)]
cd=1

# deque((0,0)) 이렇게 작성하지 말고 list 형태로 작성해야 한다.
snake=deque([(0,0)])

def move_forward(cd):
  global snake, board
  a,b=snake[0]
  #cd 방향대로 더한다.
  dx,dy=moved[cd]
  x,y=a+dx,b+dy
  if 0<=x<n and 0<=y<n:
    if is_blocked(x,y):
      return False
    snake.appendleft((x,y))
    if board[x][y]==0:
      snake.pop()
    #먹은 사과는 삭제해줘야 한다.
    else:
      board[x][y]=0
    return True
  else:
    return False

# 시계방향으로 북-동-남-서 로 list화 해놓고, 이렇게 1씩 더하고 빼서 방향을 정한다.
def change_direction(direction,cd):
  if direction=='L':
    cd=(cd-1)%4
  else:
    cd=(cd+1)%4
  return cd

def is_blocked(x,y):
  global snake
  if (x,y) in snake:
    return True
  return False
  
  
time=0
while True:
  for i in range(len(time_list)):
    if time==time_list[i]:
      cd=change_direction(direction_list[i],cd)
      #방향 바꾸고 난 다음에는 break를 해줘야 다시 방향이 바뀌지 않는다.
      break
  time+=1
  if not move_forward(cd):
    break
  
print(time)


