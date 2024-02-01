import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
tree=[[] for _ in range(n+1)]

#트리 입력받기
for _ in range(n-1):
  a,b,c=map(int,input().split())
  tree[a].append((b,c))
  tree[b].append((a,c))

#bfs로 길 찾기

#max 값을 갱신하는 방향으로
def bfs(entr):
  q=deque()
  q.append((entr,0))
  visited=[False]*(n+1)
  visited[entr]=True
  max=0

  while q:
    i,dist=q.popleft()
    if max<dist:
      max=dist
    for j, w in tree[i]:
      if not visited[j]:
        q.append((j,dist+w))
        visited[j]=True
  return max

print(bfs(1))