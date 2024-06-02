import sys
import heapq

input=sys.stdin.readline

n=int(input())
cards=[]
for i in range(n):
  a=int(input())
  cards.append(a)

# heapq는 다음과 같이 사용한다. cards 리스트를 heap화 하여,
heapq.heapify(cards)


answer=0
while len(cards)>1:
  # heapq를 pop할 때 heap화 한 cards 리스트를 매개변수로 넣고,
  # push할 때 cards 리스트의 매개변수와 더할 값을 매개변수로 넣어 사용한다.
  a=heapq.heappop(cards)
  b=heapq.heappop(cards)
  t=a+b
  answer+=t
  heapq.heappush(cards,t)

print(answer)
