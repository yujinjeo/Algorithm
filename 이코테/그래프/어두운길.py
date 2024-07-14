import sys
import heapq

input=sys.stdin.readline

n,m=map(int,input().split())
board=[[] for _ in range(n)]
q=[]
parent=[i for i in range(n)]

total=0
for _ in range(m):
  r,k,dis=map(int,input().split())
  heapq.heappush(q,(dis,r,k))
  total+=dis

def find_parent(x):
  if x!=parent[x]:
    parent[x]=find_parent(parent[x])
  return parent[x]

def union(a,b):
  x=find_parent(a)
  y=find_parent(b)
  if x<y:
    parent[y]=x
  else:
    parent[x]=y

answer=0
while q:
  dis,a,b=heapq.heappop(q)
  if find_parent(a)!=find_parent(b):
    union(a,b)
    answer+=dis

print(total-answer)


