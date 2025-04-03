import sys
from collections import deque

input = sys.stdin.readline

a,b,c = map(int,input().split())
if (a+b+c)%3!=0:
    print(0)
    sys.exit()

visited=set()
ini=tuple(sorted([a,b,c]))
visited.add(ini)

def check(lst):
    a=lst[0]
    b=lst[1]
    
    if a==b or a*2==b or b*2==a:
        return None

    x1=min(a,b)*2
    x2=max(a,b)-min(a,b)
    x3=lst[2]

    return tuple(sorted([x1,x2,x3]))

q=deque([ini])
while q:
    x,y,z=q.popleft()
    if x==y==z:
        print(1)
        sys.exit()
     
    for t in [(x,y,z),(z,x,y),(y,z,x)]:
        cand = check(t)
        if not cand:
            continue
        if cand[1]==cand[0]==cand[2]:
            print(1)
            sys.exit()
        if cand not in visited:
            visited.add(cand)
            q.append(cand)

print(0)
