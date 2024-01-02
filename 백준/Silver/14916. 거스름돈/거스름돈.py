import sys

n=int(sys.stdin.readline())

dp=[-1,-1,1,-1,2,1]

if n<=5:
  print(dp[n])
else:
  for i in range(6,n+1):
    if dp[i-2]!=-1 and dp[i-5]!=-1:
      dp.append(min(dp[i-2],dp[i-5])+1)
    else:
      dp.append(max(dp[i-2],dp[i-5])+1)
  print(dp[n])  