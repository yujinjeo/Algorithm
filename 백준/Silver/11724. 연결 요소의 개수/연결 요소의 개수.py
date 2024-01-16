import sys
sys.setrecursionlimit(10**6)

n,m=map(int,sys.stdin.readline().split())

visited=[False]*(n+1)
lst=[[] for _ in range(n+1)]

for i in range(m):
  x,y=map(int,sys.stdin.readline().split())
  lst[x].append(y)
  lst[y].append(x)

def dfs(i, k):
  visited[i]=True
  for j in lst[i]:
    if not visited[j]:
      dfs(j,k)

cnt=0
k=1
for i in range(1,n+1):
  if not visited[i]:
    dfs(i,k) 
    cnt+=1
    k+=1

print(cnt)
