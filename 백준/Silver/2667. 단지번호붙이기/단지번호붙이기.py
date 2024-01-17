import sys

n=int(input())

apt=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(i,j):
  global cnt
  apt[i][j]=0
  cnt+=1
  for t in range(4):
    x=i+dx[t]
    y=j+dy[t]
    if 0<=x<n and 0<=y<n:
      if apt[x][y]==1:
        dfs(x,y)


dic={}
k=1
for i in range(n):
  for j in range(n):
    if apt[i][j]==1:
      cnt=0
      dfs(i,j)
      dic[k]=cnt
      k+=1

print(k-1)
vals=sorted(dic.values())

for val in vals:
  print(val)