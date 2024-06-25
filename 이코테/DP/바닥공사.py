# dp
# 1. 큰 문제를 작은 문제로 쪼갤 수 있다.
# 2. 작은 문제가 그 다음 문제의 답이 된다는 것이 보장되어 있다.

import sys

input = sys.stdin.readline
n=int(input())

dp=[0,1,3]
for i in range(3,n+1):
  dp.append((dp[i-2]*2+dp[i-1]*1)%796796)

print(dp[n])

