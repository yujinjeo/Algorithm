import sys
from collections import deque

input = sys.stdin.readline

n,m=map(int, input().split(' '))
board=[list(map(str,input().rstrip())) for _ in range(m)]

d=[(0,1),(0,-1),(1,0),(-1,0)]
dic={'W':0,'B':0}
visited=[[False for _ in range(n)] for _ in range(m)]

def bfs(x,y,color):
  q=deque([(x,y)])
  cnt=1
  while q:
    i,j=q.popleft()
    for dx, dy in d:
      a=i+dx
      b=j+dy
      if 0<=a<m and 0<=b<n and not visited[a][b]:
        if board[a][b]==color:
          visited[a][b]=True
          q.append((a,b))
          cnt+=1

  return cnt

for i in range(m):
  for j in range(n):
    if not visited[i][j]:
      visited[i][j]=True
      val=bfs(i,j,board[i][j])
      dic[board[i][j]]+=val**2

print(dic['W'], dic['B'])

  