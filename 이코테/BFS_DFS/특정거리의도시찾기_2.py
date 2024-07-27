import sys
from collections import deque

input = sys.stdin. readline

n,m,target,start=map(int, input().split())

distance=[0 for _ in range(n+1)]
cities=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]


for _ in range(m):
  a,b=map(int, input().split())
  cities[a].append(b)

answer=0

def bfs():
  global answer
  
  q=deque()
  visited[start]=True
  q.append((start,0))
  
  while q:
    city,dist=q.popleft()
    for a in cities[city]:
      if visited[a]==False:
        visited[a]=True
        distance[a]=dist+1
        q.append((a,dist+1))

bfs()
if distance.count(target)==0:
  print(-1)
else:
  for i in range(1,len(distance)):
    if distance[i]==target:
      print(i)
      
