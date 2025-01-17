import sys

input = sys.stdin.readline
t=int(input())
MOD=1234567

graph={
    0:[7],
    1:[2,4],
    2:[1,3,5],
    3:[2,6],
    4:[1,5,7],
    5:[2,4,6,8],
    6:[3,5,9],
    7:[0,4,8],
    8:[5,7,9],
    9:[8,6]
}


def func(n):
    if n==1: 
        return 10
    # i길이의 비밀번호가 있을 때 j에서 출발했을 때 만들 수 있는 비밀번호의 수
    dp=[[0 for i in range(10)] for _ in range(n+1)]
    dp[1]=[1 for _ in range(10)]

    for i in range(2,n+1):
        for j in range(10):
            for ad in graph[j]:
                dp[i][j]+=dp[i-1][ad]

    return sum(dp[n])%MOD
    

for _ in range(t):
    x=int(input())
    print(func(x))