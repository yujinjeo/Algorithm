n=int(input())
dp=[0,1,2,4]

for i in range(4,12):
  dp.append(dp[i-1]+dp[i-2]+dp[i-3])

ans=[0]*n
for i in range(n):
  k=int(input())
  ans[i]=dp[k]

for a in ans:
  print(a)