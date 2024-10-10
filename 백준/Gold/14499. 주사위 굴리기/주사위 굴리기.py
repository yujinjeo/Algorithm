import sys

input = sys.stdin.readline

n,m,x,y,k=map(int,input().split(' '))
lst=[0,0,0,0,0,0,0]
board=[list(map(int,input().split(' '))) for _ in range(n)]


order=list(map(int,input().split(' ')))
d=[(0,0),(0,1),(0,-1),(-1,0),(1,0)]

def change(d):
  if d==1:
    lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]= lst[4],lst[2],lst[1],lst[6],lst[5],lst[3]
  elif d==2:
    lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]= lst[3],lst[2],lst[6],lst[1],lst[5],lst[4]
  elif d==3:
    lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]= lst[5],lst[1],lst[3],lst[4],lst[6],lst[2]
  else:
    lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]= lst[2],lst[6],lst[3],lst[4],lst[1],lst[5]

for i in range(k):
  dx,dy=d[order[i]][0],d[order[i]][1]
  a=x+dx
  b=y+dy
  if 0<=a<n and 0<=b<m:
    change(order[i])
    if board[a][b]==0:
      board[a][b]=lst[6]
    else:
      lst[6]=board[a][b]
      board[a][b]=0
    x,y=a,b
    print(lst[1])
    
  

