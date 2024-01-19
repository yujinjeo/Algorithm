import sys
sys.setrecursionlimit(10**5)

n=int(input())

board=[list(map(str,sys.stdin.readline().strip())) for _ in range(n)]

visited=[[False for _ in range(n)] for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs1(i,j,A):
  global cnt
  visited[i][j]=True
  if A=='G':
    board[i][j]='R'
    
  cnt+=1
  for t in range(4):
    x=i+dx[t]
    y=j+dy[t]
    if 0<=x<n and 0<=y<n:
      if visited[x][y]==False and board[x][y]==A:
        dfs1(x,y,A)
        

ans1=[]
ans2=[]
for i in range(n):
  for j in range(n):
    if visited[i][j]==False:
      cnt=0
      dfs1(i,j,board[i][j])
      ans1.append(cnt)

visited=[[False for _ in range(n)] for _ in range(n)]

for i in range(n):
  for j in range(n):
    if visited[i][j]==False:
      cnt=0
      dfs1(i,j,board[i][j])
      ans2.append(cnt)

print(len(ans1),len(ans2))