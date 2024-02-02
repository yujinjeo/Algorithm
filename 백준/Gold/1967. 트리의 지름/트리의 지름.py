import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())

#트리 입력받기
tree=[[] for _ in range(n+1)]
leaf=[i for i in range(1,n+1)]

for _ in range(n-1):
  p,c,w=map(int,input().split())
  if p in leaf:
    leaf.remove(p)
  tree[p].append((c,w))
  tree[c].append((p,w))

#dfs
def dfs(start,visited):
  for node,weight in tree[start]:
    if visited[node]==-1:
      visited[node]=visited[start]+weight
      dfs(node,visited)


visited=[-1 for _ in range(n+1)]
visited[1]=0
dfs(1,visited)

t=visited.index(max(visited))

visited2=[-1 for _ in range(n+1)]
visited2[t]=0
dfs(t,visited2)
ans=max(visited2)

print(ans)