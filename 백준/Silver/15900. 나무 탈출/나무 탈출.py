import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
visited=[-1]*(n+1)
tree={}
for i in range(n-1):
    a,b =map(int,input().split())
    if a not in tree:
        tree[a]=[b]
    else:
        tree[a].append(b)
    if b not in tree:
        tree[b]=[a]
    else:
        tree[b].append(a)

q=deque([1])
visited[1]=0
ans=0

while q:
    isleaf=True
    x=q.popleft()
    for i in tree[x]:
        if visited[i]==-1:
            isleaf=False
            q.append(i)
            visited[i]=visited[x]+1
    if isleaf:
        ans+=visited[tree[x][0]]+1      
# print(visited)
# print(ans)
if ans%2==0:
    print('No')
else:
    print('Yes')
        
    
