import sys

input = sys.stdin.readline

# 팰린드롬은 순서를 거꾸로 읽었을 때도 원래의 수열과 동일한 문자열을 만ㄹ한다. 즉 대칭인 것.

# pypy로 한다는데..? 뭔데 이거 
# 이게 왜 dp야?? dp??

n=int(input())

lst=list(map(int,input().split(' ')))
m=int(input())
ans=[]

dp=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  dp[i][i]=1

# 차이 1일 때
for i in range(n-1):
  if lst[i]==lst[i+1]:
    dp[i][i+1]=1

gap=2
while gap<n:
  for i in range(n-gap):
    if dp[i+1][i+gap-1]==1 and lst[i]==lst[i+gap]:
      dp[i][i+gap]=1
  gap+=1

for _ in range(m):
  x,y=map(int,input().split(' '))
  print(dp[x-1][y-1])