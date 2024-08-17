dp=[0,0,1,1,2,1]

n=int(input())

def dynamic(n):
  for i in range(6,n+1):
    val=30001
    if i%5==0:
      val=min(val,dp[i//5]+1)
    if i%3==0:
      val=min(val,dp[i//3]+1)
    if i%2==0:
      val=min(val,dp[i//2]+1)
    val=min(val,dp[i-1]+1)
    dp.append(val)

if n<=5:
  print(dp[n])
else:
  dynamic(n)
  print(dp[n])
