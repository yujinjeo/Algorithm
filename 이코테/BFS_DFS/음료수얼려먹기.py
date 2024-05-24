import sys
input=sys.stdin.readline
#음료수 얼려 먹기
#dfs로 풀어보기

n,m=map(int,input().split())

board=[input().strip() for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x,y):
  if visited[x][y]==True:
    return
  visited[x][y]=True
  for i in range(4):
    dx,dy=d[i]
    if 0<=x+dx<n and 0<=y+dy<m:
      if visited[x+dx][y+dy]==False and board[x+dx][y+dy]=='0':
        dfs(x+dx,y+dy)

answer=0
for i in range(n):
  for j in range(m):
    if board[i][j]=='0' and visited[i][j]==False:
      dfs(i,j)
      answer+=1

print(answer)
