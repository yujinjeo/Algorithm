### sol 1 : 나의 풀이
import sys

input = sys.stdin.readline

n=int(input())
m=int(input())

cnt=0
stop=1
gate=[0 for _ in range(n+1)]

for i in range(1,m+1):
  k=int(input())
  flag=0
  if stop==1:
    for r in range(k,0,-1):
      if gate[r]==0:
        gate[r]=i
        cnt+=1
        flag=1
        break
  if flag==0:
    stop=0

print(cnt)
    
    
  
    
### sol 2 : 답변 풀이 

import sys

input = sys.stdin.readline

n=int(input())
m=int(input())

parent=[i for i in range(n+1)]

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

cnt=0
stop=0

for i in range(m):
  k=int(input())
  root=find_parent(k)
  if stop==0 and root!=0:
    union(root,root-1)
    cnt+=1
  else:
    stop=1

print(cnt)
