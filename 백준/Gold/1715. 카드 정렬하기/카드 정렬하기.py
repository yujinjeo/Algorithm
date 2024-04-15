import sys
from heapq import heappush, heappop

# 우선순위 큐라는 것은 FIFO 구조를 가지는 큐에, 특정 조건을 가지는 우선순위를 만족했을 때 먼저 pop되는 자료구조이다.
# 이 개념을 구현한 것이 heap이다. heap은 새로운 값을 insert해도 항상 오름차순 혹은 내림차순으로 값을 꺼낼 수 있따.
# python에서는 heapq 모듈을 지원하고, heapify(), heappop(), heappush() 함수를 지원한다. 
# 이 문제가 어떻게 힙 개념을 정석대로 보여주는지는 책을 보고 더 공부해야 할 것 같다.

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
