import sys

input = sys.stdin.readline

n=int(input())

board=[list(map(int,input().split(' '))) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=1
d=[(1,0),(0,1)]

for i in range(n):
    for j in range(n):
        if dp[i][j]>0 and (i,j)!=(n-1,n-1):
            for dx,dy in d:
                x=dx*board[i][j]+i
                y=dy*board[i][j]+j
                if 0<=x<n and 0<=y<n:
                    dp[x][y]+=dp[i][j]

print(dp[n-1][n-1])
                

