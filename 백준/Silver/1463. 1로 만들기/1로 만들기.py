from math import floor

n=int(input())

dp=[0,0,1,1]
for i in range(4,n+1):
  minval=1e9
  if i%3==0:
    minval=min(minval,dp[floor(i/3)])
  if i%2==0:
    minval=min(minval,dp[floor(i/2)])
  minval=min(minval,dp[i-1])
  dp.append(minval+1)


print(dp[n])