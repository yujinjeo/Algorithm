import sys
input = sys.stdin.readline
n,s,m=map(int,input().split(' '))

lst=list(map(int,input().split(' ')))

# dp[i][v] : i번째까지 고려했을 때 v 볼륨을 가질 수 있는지 여부
dp=[[False] *(m+1) for _ in range(n+1)]

dp[0][s]=True

def dynamic():
    for i in range(1,n+1):
        for j in range(m+1):
            c=dp[i-1][j]
            if c:
                if 0<=j+lst[i-1]<=m:
                    dp[i][j+lst[i-1]]=True
                if m>=j-lst[i-1]>=0:
                    dp[i][j-lst[i-1]]=True

dynamic()
ans=-1
for i in range(m,-1,-1):
    if dp[n][i]:
        ans=i
        break

print(ans)
