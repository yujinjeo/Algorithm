import sys
import heapq

input = sys.stdin.readline

n,m= map(int,input().split())

parent=[i for i in range(n+1)]

graph=[]
for _ in range(m):
  a,b,dist=map(int,input().split())
  heapq.heappush(graph,(dist,a,b))

# 같은 그룹인지 확인 : parent 확인
def find_parent(x):
  if parent[x]!=x:
    parent[x]=find_parent(parent[x])
  return parent[x]

def union(a,b):
  a=find_parent(a)
  b=find_parent(b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

distance=[]

while graph:
  dis,a,b=heapq.heappop(graph)
  if find_parent(a)!=find_parent(b):
    union(a,b)
    distance.append(dis)

distance.sort(reverse=True)
answer=sum(distance[1:])
print(answer)
