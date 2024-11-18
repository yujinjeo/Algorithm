

n= int(input())

def func():
  s1, s2, target = map(str,input().rstrip().split(' '))
  n1, n2 = len(s1), len(s2)
  
  dp = [[False for _ in range(n2+1)] for _ in range(n1+1)]
  dp[0][0]=True

  for i in range(n1+1):
    for j in range(n2+1):
      if i>0 and s1[i-1]==target[i+j-1] and dp[i-1][j]:
        dp[i][j]=True

      if j>0 and s2[j-1] ==target[i+j-1] and dp[i][j-1]:
        dp[i][j]=True
        
  if dp[n1][n2]:
    return 'yes'
  return 'no'

for t in range(n):
  result=func()
  print(f"Data set {t+1}: {result}")

  
