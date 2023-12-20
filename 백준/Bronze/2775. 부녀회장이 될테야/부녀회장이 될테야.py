import sys

t=int(sys.stdin.readline())
ans=[]

def dp(apt,k,n):
  for j in range(1,k+1):
    for i in range(n+1):
      apt[j][i]=sum(apt[j-1][:i+1])
  return apt[k][n]

for _ in range(t):
  k=int(sys.stdin.readline())
  n=int(sys.stdin.readline())

  apt=[[0]*(n+1) for _ in range(k+1)]
  apt[0]=[i for i in range(n+1)]
  ans.append(dp(apt,k,n))

for a in ans:
  print(a)