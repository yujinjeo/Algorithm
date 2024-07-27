import sys
from collections import deque

input = sys.stdin.readline

n,m=map(int, input().split())
board=[list(map(str,input().rstrip())) for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]

d = [(0,1),(1,0), (0,-1),(-1,0)]

def findRoute(start_x, start_y):
  visited[start_x][start_y]=True
  q=deque()
  q.append((start_x,start_y,1))
  
  while q:
    x,y,cnt=q.popleft()
    if x==n-1 and y==m-1:
      return cnt
    for dx,dy in d:
      a,b=x+dx,y+dy
      if 0<=a<n and 0<=b<m and visited[a][b]==False and board[a][b]=='1':
        visited[a][b]=True
        q.append((a,b,cnt+1))

print(findRoute(0,0))
        
        
        
    



