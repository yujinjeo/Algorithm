# dp
# 1. 큰 문제를 작은 문제로 쪼갤 수 있다.
# 2. 작은 문제가 그 다음 문제의 답이 된다는 것이 보장되어 있다.

import sys

n= int(sys.stdin.readline())

lst = [0,1,1,1,2,1]

for i in range(6, n+1):
  val = lst[i-1]
  if i%2==0:
    val=min(val, lst[i//2])
  if i%3==0:
  val=min(val, lst[i//3])
  if i%5==0:
    val=min(val, lst[i//5])
  lst.append(val+1)

print(lst[n])
