n,k=map(int,input().split(' '))

lst=[[0,0]]+list(list(map(int, input().split(' '))) for _ in range(n))
lst.sort(key=lambda x : x[0])
dp=[[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(1,k+1):
  for j in range(1,n+1):
    w=lst[j][0]
    v=lst[j][1]
    if i>=w:
      dp[i][j]=max(dp[i][j-1], dp[i-w][j-1]+v)
    else:
      dp[i][j]=dp[i][j-1]

print(dp[k][n])

