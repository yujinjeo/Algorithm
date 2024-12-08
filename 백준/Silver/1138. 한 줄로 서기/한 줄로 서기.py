
n=int(input())

lst=list(map(int,input().split(' ')))

visited=[False]*n
ans=[0 for _ in range(n)]

for i in range(n):
  idx=0
  unvisited=-1
  for j in range(n):
    if not visited[j]:
      unvisited+=1
    if lst[i]==unvisited:
      idx=j
      break
  visited[idx]=True
  ans[idx]=i+1

print(*ans)
  


