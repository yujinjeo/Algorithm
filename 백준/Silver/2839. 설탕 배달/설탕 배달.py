import sys

MAX_INT=sys.maxsize

n=int(input())
#    0  1  2 3  4 5
dp=[-1,-1,-1,1,-1,1]

if n<=5:
  print(dp[n])
else:
  for i in range(6,n+1):
    a,b=MAX_INT,MAX_INT
    if dp[i-3]!=-1:
      a=dp[i-3]+1
    if dp[i-5]!=-1:
      b=dp[i-5]+1
    if a==MAX_INT and b==MAX_INT:
      dp.append(-1)
      continue
    dp.append(min(a,b))
  print(dp[n])