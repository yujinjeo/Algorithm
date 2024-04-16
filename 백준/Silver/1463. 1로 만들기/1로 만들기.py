import sys

n=int(sys.stdin.readline())

dp=[0,0,1,1]

if n<4:
  print(dp[n])
else:
  for i in range(4,n+1):
    cand=[dp[i-1]+1]
    if i%2==0:
      cand.append(dp[i//2]+1)
    if i%3==0:
      cand.append(dp[i//3]+1)
    dp.append(min(cand))
  print(dp[n])