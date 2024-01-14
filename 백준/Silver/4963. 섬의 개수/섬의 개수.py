import sys
sys.setrecursionlimit(10**5)
dx=[1,1,-1,-1,0,0,1,-1]
dy=[1,-1,1,-1,1,-1,0,0]

def dfs(i,j):
  global board, w, h
  if board[i][j]==1:
    board[i][j]=0
    for t in range(8):
      x=i+dx[t]
      y=j+dy[t]
      if 0<=x<h and 0<=y<w:
        dfs(x,y)
  else:
    return

  
ans=[]

while True:
  w,h=map(int,sys.stdin.readline().split())
  if w==0 and h==0:
    break
  board=[list(map(int, sys.stdin.readline().split())) for _ in range(h)]
  cnt=0
  for i in range(h):
    for j in range(w):
      if board[i][j]==1:
        dfs(i,j)
        cnt+=1
  ans.append(cnt)

for a in ans:
  print(a)