import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n,m=map(int,input().split(' '))
board=[]

house=[]
chicken=[]
for i in range(n):
  lst=list(map(int,input().split(' ')))
  for j in range(n):
    if lst[j]==1:
      house.append((i,j))
    if lst[j]==2:
      chicken.append((i,j))
  board.append(lst)
  

d=[(0,1),(0,-1),(1,0),(-1,0)]
answer=1e9

def find(i,j,chicks):
  dist=1e9
  for a,b in chicks:
    d=abs(i-a)+abs(j-b)
    dist=min(d,dist)
  return dist
  
  # visited=[[False for _ in range(n)] for _ in range(n)]
  # visited[i][j]=True
  # q=deque([(i,j,0)])
  # while q:
  #   x,y,cnt=q.popleft()
  #   if (x,y) in chicks:
  #     return cnt
    
  #   for k in range(4):
  #     a=x+d[k][0]
  #     b=y+d[k][1]
  #     if 0<=a<n and 0<=b<n:
  #       if visited[a][b]==False:
  #         q.append((a,b,cnt+1))
  #         visited[a][b]=True

c_lst=list(combinations(chicken, m))

for chicks in c_lst:
  cand=0
  for i in range(len(house)):
    cand+=find(house[i][0],house[i][1], chicks)
  answer=min(answer,cand)
          
print(answer)
  

