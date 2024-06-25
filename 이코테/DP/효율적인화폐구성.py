# dp
# 1. 큰 문제를 작은 문제로 쪼갤 수 있다.
# 2. 작은 문제가 그 다음 문제의 답이 된다는 것이 보장되어 있다.

import sys

input = sys.stdin.readline
n,m=map(int,input().split())

lst=[int(input()) for _ in range(n)]

dp=[10001 for i in range(m+1)]
for i in lst:
  if i<m+1:
    dp[i]=1

for i in range(1,m+1):
  for j in range(len(lst)):
    if i-lst[j]>0:
      dp[i]=min(dp[i],dp[i-lst[j]]+1)


if dp[m]>10000:
  print(-1)
else:
  print(dp[m])

