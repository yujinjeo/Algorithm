import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))


#sol 1
dp=[0 for _ in range(n)]
dp[0], dp[1]= lst[0],lst[1]

for i in range(n):
  cand=i-2
  if i-3>=0 and dp[cand]<dp[i-3]:
    cand=i-3
  dp[i]=lst[i]+dp[cand]

print(max(dp))


#sol 2 - 'Ne5s.log'라는 벨로그에서 찾은 풀이
dp=[0 for _ in range(300)]
dp[0]=lst[0]
dp[1]=max(lst[0],lst[1])

for i in range(2,n):
  dp[i]=max(dp[i-1], dp[i-2]+lst[i])

print(dp[n-1])
