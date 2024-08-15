import sys
from bisect import bisect_left

input = sys.stdin.readline

n,m=map(int,input().split())

lst=[0 for _ in range(n)]

for i in range(n):
  lst[i]=int(input())

lst.sort()

def count_(cand):
  cnt=1
  current=lst[0]

  for i in range(n):
    if current+cand<=lst[i]:
      current=lst[i]
      cnt+=1

  return cnt

answer=0
def bisect(start,end):
  global answer
  
  if start>end:
    return
  mid=(start+end)//2

  val=count_(mid)
  if val>=m:
    answer=max(answer,mid)
    bisect(mid+1,end)
  else:
    bisect(start,mid-1)

bisect(1,lst[-1]-lst[0])
print(answer)
