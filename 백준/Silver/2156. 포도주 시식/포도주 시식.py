import sys

input = sys.stdin.readline

n=int(input())
lst=[0 for _ in range(n)]
dp=[0 for _ in range(n+1)]
for i in range(n):
    lst[i]=int(input())

if n<3:
    print(sum(lst[:n]))
else:
    dp[1]=lst[0]
    dp[2]=lst[0]+lst[1]

    for i in range(3,n+1):
        dp[i]=max(dp[i-1],dp[i-2]+lst[i-1],dp[i-3]+lst[i-2]+lst[i-1])

    print(dp[n])
