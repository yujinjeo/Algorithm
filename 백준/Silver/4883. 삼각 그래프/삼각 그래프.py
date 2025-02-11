import sys

input = sys.stdin.readline

d=[(-1,-1),(-1,0),(-1,1),(0,-1)]
INF = float('inf')
def func(n):
    lst=[list(map(int,input().split(' '))) for _ in range(n)]
    dp=[[INF,INF,INF] for _ in range(n)]
    dp[0][1]=lst[0][1]
    dp[0][2]=lst[0][1]+lst[0][2]
    
    for i in range(1,n):
        for j in range(3):
            v=INF
            for dx,dy in d:
                a=i+dx
                b=j+dy
                if 0<=b<3:
                    v=min(v,dp[a][b])
            dp[i][j]=v+lst[i][j]

    return dp[n-1][1]

ans=[0]
while True:
    n=int(input())
    if n==0 : 
        break
    ans.append(str(func(n)))

for i in range(1,len(ans)):
    print(str(i)+". "+ans[i])

    