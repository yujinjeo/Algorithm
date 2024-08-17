import sys

input =sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

dp=[0 for i in range(n)]
for i in range(n):
  cand1, cand2, cand3=0,lst[i],lst[i]
  
  if i-1>=0:
    cand1+=dp[i-1]
  if i-2>=0:
    cand2+=dp[i-2]
  if i-3>=0:
    cand3+=dp[i-3]

  dp[i]=max(cand1,cand2,cand3)

print(dp[n-1])
