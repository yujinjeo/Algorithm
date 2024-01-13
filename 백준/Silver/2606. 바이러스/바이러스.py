import sys

computers=int(sys.stdin.readline())
connections=int(sys.stdin.readline())
board=[[0 for _ in range(computers+1)] for _ in range(computers+1)]

for _ in range(connections):
  i,j=map(int,sys.stdin.readline().split())
  board[i][j]=1
  board[j][i]=1

lst=[0 for _ in range(computers+1)]

cnt=0
def dfs(n):
  lst[n]=1
  global cnt
  for i in range(1,computers+1):
    if board[n][i]==1:
      board[n][i]=0
      if lst[i]==0:
        cnt+=1
        dfs(i)
    else:
      continue

dfs(1)
print(cnt)