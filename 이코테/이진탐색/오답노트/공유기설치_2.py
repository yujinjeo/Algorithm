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

  # while True 안에서 bisect_left를 하였더니 시간초과가 났다. for 문으로 바꿔서 해결.
  for i in range(n):
    if current+cand<=lst[i]:
      current=lst[i]
      cnt+=1

  return cnt

answer=0
# 원인모를 오답이 나왔는데, 인덱스를 측정하는 것이 아니라 길이를 측정하는 것이기 때문에 start를 0이 아니라 1로, end를 n-1이 아니라 가장 큰 gap을 해야 한다.
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
