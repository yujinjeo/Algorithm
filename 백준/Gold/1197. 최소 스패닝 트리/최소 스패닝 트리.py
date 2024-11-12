import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

v,e=map(int,input().split(' '))
edges=[]

for _ in range(e):
  x,y,c=map(int,input().split(' '))
  edges.append((x,y,c))

edges.sort(key=lambda x: x[2])

# union-find 방식으로 풀어보기- 최소-신장 트리를 찾기 위해
parent=[i for i in range(v+1)]
 
def get_parent(x):
  if parent[x]==x:
    return x
  parent[x]=get_parent(parent[x])
  return parent[x]

def same_parent(a,b):
  return get_parent(a)==get_parent(b)

def union_parent(a,b):
  
  a=get_parent(a)
  b=get_parent(b)
  
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

ans=0

for x,y,c in edges:
  if not same_parent(x,y):
    union_parent(x,y)
    ans+=c

print(ans)
