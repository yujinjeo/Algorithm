import sys
from collections import deque

input=sys.stdin.readline

n,l,r=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]

#board 전체에서 옆 칸과의 차이가 얼마나 나는지 확인해야 한다.  bfs로 구역을 찾아야 한다. visited..? 는 있어야 
d=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(i,j):
  q=deque()
  q.append((i,j))
  land=[(i,j)]
  while q:
    x,y=q.popleft()
    for i in range(4):
      a=x+d[i][0]
      b=y+d[i][1]
      if 0<=a<n and 0<=b<n and visited[a][b]==False:
        if l<=abs(board[a][b]-board[x][y])<=r:
          visited[a][b]=True
          land.append((a,b))
          q.append((a,b))
  return land


answer=0
while True:
  visited=[[False for _ in range(n)] for _ in range(n)]
  today=[]
  
  for i in range(n):
    for j in range(n):
      if visited[i][j]==False:
        visited[i][j]=True
        land=bfs(i,j)
        if len(land)>=2:
          today.append(land)
  if today==[]:
    break
          
  #today 각 랜드들 값을 넣기
  for land in today:
    lsum=sum(board[x][y] for x,y in land)
    val=lsum//len(land)
    for i,j in land:
      board[i][j]=val
  answer+=1

print(answer)
