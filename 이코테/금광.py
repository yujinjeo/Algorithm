import sys
input=sys.stdin.readline

t=int(input())

def dymp(dp,n,m):
  answer=0
  for j in range(1,m+1):
    for i in range(1,n+1):
      dp[i][j]=max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])+dp[i][j]
      answer=max(answer,dp[i][j])
  return answer
  
for _ in range(t):
  n,m=map(int,input().split())
  dp=[[0 for _ in range(m+2)] for _ in range(n+2)]
  tmp=list(map(int,input().split()))
  z=0
  for i in range(1,n+1):
    for j in range(1,m+1):
      dp[i][j]=tmp[z]
      z+=1
  answer=dymp(dp,n,m)
  print(answer)
