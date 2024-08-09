import sys
import heapq

input = sys.stdin.readline

n=int(input())
lst=[]
for _ in range(n):
  lst.append(int(input()))

heapq.heapify(lst)
answer=0
while True:
  if len(lst)<2:
    break
  a=heapq.heappop(lst)
  b=heapq.heappop(lst)
  answer+=(a+b)
  heapq.heappush(lst,a+b)

print(answer)
