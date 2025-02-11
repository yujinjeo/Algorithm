import sys

input = sys.stdin.readline

n=int(input())

dp=[False, False, True, False, True, True]+[False]*(n-5)

for i in range(6,n+1):
    if False in [dp[i-1], dp[i-3], dp[i-4]]:
        dp[i]=True
    else:
        dp[i]=False

if dp[n]:
    print('SK')
else:
    print('CY')