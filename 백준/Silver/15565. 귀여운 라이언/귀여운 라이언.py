import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())
lst = list(map(int,input().split()))

il1=deque()
# 처음 만들기
cnt1=0
for i in range(n):
    if lst[i]==1:
        cnt1+=1
        il1.append(i)
    if cnt1==k:
        break
        
if len(il1)<k:
    print(-1)
    sys.exit()
elif k==1:
    print(1)
    sys.exit()
    
current1=il1[-1]-il1[0]+1
start1=il1[-1]

for i in range(start1+1,n):
    if lst[i]==1:
        il1.popleft()
        il1.append(i)
        current1=min(current1, il1[-1]-il1[0]+1)

print(current1)
        