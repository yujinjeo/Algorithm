import sys
# 중복조합으로 풀려고 했지만 dp 였다...
input = sys.stdin.readline

n=int(input())
# dp[i][j] : i 글자수일 때 j 수를 마지막으로 하는 총 개수
dp=[[1 for _ in range(10)] for _ in range(n+1)]

for i in range(2,n+1):
    for j in range(1,10):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]

print(sum(dp[n])%10007)

    