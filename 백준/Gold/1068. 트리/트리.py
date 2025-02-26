import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree={}
for i in range(n):
    tree[i]=[]

parent=list(map(int,input().split()))
root=0

for i in range(n):
    p=parent[i]
    if p==-1:
        root=i
        continue
    tree[p].append(i)

rm=int(input())
q=deque([rm])
visited=[False]*(n)
visited[rm]=True
if rm!=root:
    tree[parent[rm]].remove(rm)

while q:
    x=q.popleft()
    for i in tree[x]:
        if not visited[i]:
            visited[i]=True
            q.append(i)
    tree[x]=[]
            
ans=0
for i in range(n):
    if not tree[i] and not visited[i]:
        ans+=1
        
print(ans)

