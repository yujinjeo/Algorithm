import sys

input = sys.stdin.readline

t,w=map(int,input().split(' '))

# dp[i][j] i시간 까지 고려했을 때, j 번 움직였을 때의 최대 자두 수/
dp=[[0 for _ in range(w+1)] for _ in range(t+1)]
lst=[0]+[int(input()) for _ in range(t)]

dp[1][0]=lst[1]%2
dp[1][1]=lst[1]//2

for i in range(2,t+1):
    for j in range(w+1):
        gain=lst[i]%2 if j%2==0 else lst[i]//2
        dp[i][j]=max(dp[i-1][:j+1])+gain

print(max(dp[t]))