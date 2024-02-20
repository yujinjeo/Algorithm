import sys
from collections import deque

input=sys.stdin.readline

#트리 만들기
n,k=map(int,input().split())
tree=[[] for _ in range(n)]

for i in range(n-1):
  a,b=map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)

apple=list(map(int,input().split()))
visited=[False]*n
ans=0

#bfs
def bfs():
  global ans
  q=deque()
  q.append((0, 0))
  visited[0]=True

  while q:
    node, dist=q.popleft()
    ans+=apple[node]
    for i in tree[node]:
      if visited[i]==False and dist+1<=k:
        q.append((i,dist+1))
        visited[i]=True

bfs()
print(ans)
        