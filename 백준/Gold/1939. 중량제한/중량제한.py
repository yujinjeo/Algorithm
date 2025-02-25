import sys
from collections import deque

input = sys.stdin.readline

n,m=map(int,input().split())

dic={}
minv = 1e10
maxv = 0

for _ in range(m):
    a,b,c=map(int,input().split())
    minv=min(minv, c)
    maxv=max(maxv, c)
    
    if a not in dic:
        dic[a]=[[b,c]]
    else:
        dic[a].append([b,c])
    
    if b not in dic:
        dic[b]=[[a,c]]
    else:
        dic[b].append([a,c])

s,e=map(int,input().split())

def check(x):
    visited=[False]*(n+1)
    q=deque([s])
    visited[s]=True
    while q:
        a=q.popleft()
        if a==e:
            return True
        for b,c in dic[a]:
            if not visited[b] and c>=x:
                q.append(b)
                visited[b]=True
    return False

ans=0
def bin(start,end):
    global ans
    if start>end:
        return
    mid=(start + end)//2
    if check(mid):
        ans=mid
        bin(mid+1, end)
    else:
        bin(start, mid-1)

bin(minv, maxv)
print(ans)


