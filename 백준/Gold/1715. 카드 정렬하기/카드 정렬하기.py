import sys
from heapq import heappush, heappop

n=int(sys.stdin.readline())
packs=[]
answer=0

for _ in range(n):
  heappush(packs,int(sys.stdin.readline()))

if n==1:
  answer=0
else:
  while len(packs)>1:
    fir=heappop(packs)
    sec=heappop(packs)
    answer+=fir+sec
    heappush(packs,fir+sec)

print(answer)