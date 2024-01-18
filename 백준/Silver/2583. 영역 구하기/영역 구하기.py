import sys
sys.setrecursionlimit(10**5)

m,n,k=map(int,sys.stdin.readline().split())

board=[[0 for _ in range(n)] for _ in range(m)]

for i in range(k):
  x1,y1,x2,y2=map(int, sys.stdin.readline().split())
  for y in range(y1,y2):
    board[y][x1:x2]=[1]*(x2-x1)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(i,j):
  global k
  board[i][j]=1
  k+=1
  for t in range(4):
    x=i+dx[t]
    y=j+dy[t]
    if 0<=x<m and 0<=y<n:
      if board[x][y]==0:
        dfs(x,y)




cnt=0
ans=[]

for i in range(m):
  for j in range(n):
    if board[i][j]==0:
      k=0
      dfs(i,j)
      ans.append(k)
      cnt+=1

print(cnt)

for a in sorted(ans):
  print(a,end=" ")