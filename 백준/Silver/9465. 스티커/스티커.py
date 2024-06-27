import sys

input = sys.stdin.readline
t=int(input())
answer=[]

for _ in range(t):
  n=int(input())
  lst=[list(map(int, input().split(' '))) for _ in range(2)]
  
  dp=[[0 for _ in range(n)] for _ in range(2)]
  dp[0][0]=lst[0][0]
  dp[1][0]=lst[1][0]

  for i in range(1,n):
    dp[0][i]=max(lst[0][i]+dp[1][i-1],dp[0][i-1])
    dp[1][i]=max(lst[1][i]+dp[0][i-1], dp[1][i-1])

  answer.append(max(dp[0][n-1], dp[1][n-1]))

for a in answer:
  print(a)
  