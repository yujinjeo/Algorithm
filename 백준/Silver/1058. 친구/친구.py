import sys

input = sys.stdin.readline

n = int(input())
board=[list(map(str,input().rstrip())) for _ in range(n)]
for i in range(n):
  for j in range(i, n):
    if i!=j and board[i][j]=='N':
      for k in range(n):
        if board[i][k]==board[k][j]=='Y':
          board[i][j]=board[j][i]='2'

maxv=0
for i in range(n):
  maxv=max(n-board[i].count('N'),maxv)

print(maxv)

