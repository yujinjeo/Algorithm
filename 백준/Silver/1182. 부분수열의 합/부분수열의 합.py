import sys
from itertools import combinations

input = sys.stdin.readline

n,s=map(int,input().split(' '))
lst=list(map(int,input().split(' ')))
answer=0
for size in range(n,0,-1):
  lsts= combinations(lst,size)
  for cand in lsts:
    if sum(cand)==s:
      answer+=1


print(answer)
