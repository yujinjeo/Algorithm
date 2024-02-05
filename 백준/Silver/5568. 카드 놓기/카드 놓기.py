import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
k=int(input())
cards=[]
for _ in range(n):
  cards.append(input().strip())

ans=[]

def backt(picked, dpt, s):
  if dpt==k:
    if s not in ans:
      ans.append(s)
    return
  for j in range(n):
    if j not in picked:
      picked.append(j)
      backt(picked,dpt+1,s+cards[j])
      picked.pop()

for i in range(n):
  picked=[i]
  backt(picked,1,cards[i])

print(len(ans))