n=int(input())
lst=list(map(int,input().split()))
dp=[lst[i] for i in range(n)]

for i in range(1,n):
  for j in range(i):
    if lst[i]>lst[j]:
      dp[i]=max(dp[i],dp[j]+lst[i])

print(max(dp))