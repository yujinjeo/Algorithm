import sys
from collections import deque

n,m=map(int,input().split(' '))
r,c,dir=map(int,input().split(' '))
board=[list(map(int,input().split(' '))) for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
visited[r][c]=True
d=[(-1,0),(0,1),(1,0),(0,-1)]
answer=1
q=deque([(r,c,dir)])
while q:
  x,y,dir=q.popleft()
  # 현 방향이 아니라 왼쪽부터 탐색 ** 반시계방향으로 90도 회전한 후, 바라보는 방향을 기준으로 전진하는 것이므로, 현 방향이 아니라 먼저 왼쪽으로 회전한 다음에 전진해야 한다.!!
  for i in range(1,5):
    tmpd=(dir-i)%4
    dx,dy=d[tmpd]
    a=x+dx
    b=y+dy
    if 0<=a<n and 0<=b<m and visited[a][b]==False and board[a][b]==0:
      visited[a][b]=True
      q.append((a,b,tmpd))
      answer+=1
      break
  if list(q)==[]:
    dx,dy=d[dir]
    if 0<=x-dx<n and 0<=y-dy<m and board[x-dx][y-dy]!=1:
      q.append((x-dx,y-dy,dir))

print(answer)
