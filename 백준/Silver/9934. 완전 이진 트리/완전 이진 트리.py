import sys
from collections import deque

k=int(input())

n=2**(k)-1
lst=list(map(int,sys.stdin.readline().split()))
ans=[[] for _ in range(k)]
start=0
end=n-1
mid=(end-start+1)//2

q=deque()
q.append((start,mid,end,0))

while q:
  s,m,e,w=q.popleft()
  if w==k:
    break
  ans[w].append(lst[m])
  q.append((s,(m-1-s+1)//2+s,m-1,w+1))
  q.append((m+1,(e-m-1+1)//2+m+1,e,w+1))

for i in range(k):
  print(*ans[i])

