import sys
from collections import deque
input=sys.stdin.readline

#미로 탈출
#최소OO 문제는 반드시 bfs..ㅎㅎ

n,m=map(int,input().split())

maze=[list(input().strip()) for _ in range(n)]
visited=[[False for i in range(m)] for _ in range(n)]
d=[(0,1),(0,-1),(1,0),(-1,0)]
time=0
q=deque([(0,0,0)])

while q:
  x,y,t=q.popleft()
  if x==n-1 and y==m-1:
    time=t
    break
  visited[x][y]=True
  for i in range(4):
    dx,dy=d[i]
    if 0<=x+dx<n and 0<=y+dy<m:
      if visited[x+dx][y+dy]==False and maze[x+dx][y+dy]=='1':
        q.append((x+dx,y+dy,t+1))

print(time+1)
        
