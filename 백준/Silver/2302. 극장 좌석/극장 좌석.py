n=int(input())
v=int(input())
vips=set()
for i in range(v):
    vips.add(int(input()))

dp=[1 for i in range(n+1)]

for i in range(2,n+1):
    if i in vips:
        dp[i]=dp[i-1]
        continue
    dp[i]=dp[i-1]
    if i-1 not in vips:
        dp[i]+=dp[i-2]
    
print(dp[n])
    

