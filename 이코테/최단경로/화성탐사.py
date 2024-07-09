import sys
import heapq

input = sys.stdin.readline

t = int(input())
INF=int(1e9)
d=[(0,1),(0,-1),(1,0),(-1,0)]

answer=[0 for _ in range(t)]
def dijkstra(board,n):
  distance=[[INF for _ in range(n)] for _ in range(n)]
  distance[0][0]=board[0][0]
  q=[]
  heapq.heappush(q,(distance[0][0],0,0))
  while q:
    dis,x,y=heapq.heappop(q)
    for i in range(4):
      dx,dy=d[i]
      if 0<=x+dx<n and 0<=y+dy<n:
        if distance[x+dx][y+dy]>distance[x][y]+board[x+dx][y+dy]:
          distance[x+dx][y+dy]=distance[x][y]+board[x+dx][y+dy]
          heapq.heappush(q,(distance[x+dx][y+dy],x+dx,y+dy))
  return distance[n-1][n-1]
  
  

for i in range(t):
  n=int(input())
  board=[list(map(int,input().split(' '))) for _ in range(n)]
  answer[i]=dijkstra(board,n)

for a in answer:
  print(a)
  




