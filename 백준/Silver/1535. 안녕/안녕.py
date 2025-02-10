import sys

n=int(input())

lose = [0]+list(map(int,input().split(' ')))
happy = [0]+list(map(int, input().split(' ')))

# dp[i][j] : i까지 고려했을 때, j 체력에서 가질 수 있는 최대 기쁨
dp=[[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if j+lose[i]<=100:
            dp[i][j]=max(dp[i-1][j+lose[i]]+happy[i], dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][1])

