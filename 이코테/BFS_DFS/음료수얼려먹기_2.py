import sys
from time import time
from collections import deque

input = sys.stdin.readline
n,m=map(int, input().split())
board=[list(map(str,input().rstrip())) for _ in range(n)]
d=[(1,0),(0,1),(-1,0),(0,-1)]


visited=[[False for _ in range(m)] for _ in range(n)]
def dfs(x,y):
  for dx,dy in d:
    a=x+dx
    b=y+dy
    if 0<=a<n and 0<=b<m and visited[a][b]==False and board[a][b]=='0':
      visited[a][b]=True
      dfs(a,b)

# dfs 시간 : 4.38690185546875e-05
start_d_t=time()
cnt=0
for i in range(n):
  for j in range(m):
    if visited[i][j]==False and board[i][j]=='0':
      visited[i][j]=True
      dfs(i,j)
      cnt+=1
end_d_t=time()
print(cnt)
print(end_d_t-start_d_t)

###########################################################################
###########################################################################

visited=[[False for _ in range(m)] for _ in range(n)]
def bfs(x,y):
  q=deque([(x,y)])
  while q:
    i,j=q.popleft()
    for dx, dy in d:
      a=i+dx
      b=j+dy
      if 0<=a<n and 0<=b<m and visited[a][b]==False and board[a][b]=='0':
        visited[a][b]=True
        q.append((a,b))

# bfs 시간 : 6.008148193359375e-05
cnt=0
start_b_t=time()
for i in range(n):
  for j in range(m):
    if visited[i][j]==False and board[i][j]=='0':
      visited[i][j]=True
      bfs(i,j)
      cnt+=1
end_b_t=time()
print(cnt)
print(end_b_t-start_b_t)
