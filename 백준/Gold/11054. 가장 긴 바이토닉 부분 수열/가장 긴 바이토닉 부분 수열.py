n=int(input())

lst=list(map(int,input().rstrip().split(' ')))

# dp[i]는 lst[i]까지 고려했을 때 최대 길이, 
dpa=[1 for i in range(n)]
dpd=[1 for i in range(n)]

if n<2:
    print(1)
else:
    for i in range(1,n):
        for j in range(i):
            if lst[i]>lst[j]:
                dpa[i]=max(dpa[i],dpa[j]+1)
    
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if lst[i]>lst[j]:
                dpd[i]=max(dpd[i],dpd[j]+1)
    
    ans=0
    for i in range(n):
        ans=max(ans, dpa[i]+dpd[i]-1)
    print(ans)