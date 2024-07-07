import sys

input=sys.stdin.readline
n=int(input())
m=int(input())
INF=int(1e9)
board=[[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
  board[i][i]=0

for i in range(m):
  a,b,c=map(int,input().split())
  board[a][b]=min(board[a][b],c)

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      board[i][j]=min(board[i][j], board[i][k]+board[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    if board[i][j]==INF:
      board[i][j]=0
    print(board[i][j],end=' ')
  print()
