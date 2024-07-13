import sys

input = sys.stdin.readline

n,m=map(int,input().split())

board=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
  board[i][1:n+1] = list(map(int,input().split()))

parent=[i for i in range(n+1)]

def find_parent(x):
  if x!=parent[x]:
    parent[x]=find_parent(parent[x])
  return parent[x]

def union(a,b):
  a=find_parent(a)
  b=find_parent(b)
  if b>a:
    parent[b]=a
  else:
    parent[a]=b


for i in range(1,n+1):
  for j in range(1,n+1):
    if board[i][j]==1:
      union(i,j)

lst=list(map(int,input().split()))
group=parent[lst[0]]
flag=0
for i in range(1,len(lst)):
  if parent[lst[i]]!=group:
    print('NO')
    flag=1
    break
if flag==0:
  print('YES')
