# dp
# 1. 큰 문제를 작은 문제로 쪼갤 수 있다.
# 2. 작은 문제가 그 다음 문제의 답이 된다는 것이 보장되어 있다.

import sys

input = sys.stdin.readline

n= int(input())
lst = list(map(int, input().split(' ')))

dp = [lst[0],lst[1],lst[2]+lst[0],lst[3]+max(lst[1],lst[0])]

for i in range(4,n):
  dp.append(lst[i]+max(dp[i-2],dp[i-3]))

print(max(dp))
