# 플로이드 워셜 알고리즘 복습 
# 한 지점에서 다른 특정 지점까지의 최단 거리를 구하는 알고리즘에는 다익스트라가 사용되었다면, 
# 모든 지점에서 모든 지점까지에 대한 최단거리를 찾고 싶을 때에는 플로이드-워셜 알고리즘을 사용한다.
# 대표적인 dp 알고리즘이며, 가중치 그래프에서 최단 거리를 반복적으로 갱신하면서 최적의 값을 찾아나간다. 
# 반대로 다익스트라는 그리디 알고리즘이다. 

import sys

input = sys.stdin.readline

n = int(input())
m=int(input())
INF=int(1e9)
board=[[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
  board[i][i]=0

for _ in range(m):
  i,j,c=map(int,input().split(' '))
  board[i][j]=min(board[i][j],c)

def alg(x):
  for i in range(1,n+1):
     for j in range(1,n+1):
       board[i][j]=min(board[i][j],board[i][x]+board[x][j])

for i in range(1,n+1):
  alg(i)

for i in range(1,n+1):
  for j in range(1,n+1):
    if board[i][j]==INF:
      board[i][j]=0

for i in range(1,n+1):
  print(*board[i][1:])
