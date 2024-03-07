import sys

n,m=map(int,sys.stdin.readline().split())

board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

d={(0,-1),(-1,0),(-1,-1)}

dp=[[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    maxval=0
    for dx,dy in d:
      x=j+dx
      y=i+dy
      if 0<=x<m and 0<=y<n:
        maxval=max(maxval,dp[y][x])
    dp[i][j]=board[i][j]+maxval

print(dp[n-1][m-1])
