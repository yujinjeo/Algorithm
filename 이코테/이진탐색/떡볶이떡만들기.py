## 최적화문제를 결정 문제로 바꾸는 파라메트릭 서치를 이진탐색으로!

import sys

input=sys.stdin.readline

n,m=map(int,input().split(' '))
lst=list(map(int,input().split(' ')))


start=0
end=max(lst)
answer=0

while (start<=end):
  middle = (start+end)//2
  total=0
  for i in range(n):
    if middle<lst[i]:
      total+=lst[i]-middle
  if total<m:
    end=middle-1
  else:
    answer=middle
    start=middle+1

print(answer)
