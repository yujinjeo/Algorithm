import sys

input = sys.stdin.readline

n,d=map(int, input().split(' '))

dp=[i for i in range(d+1)]

lst=[list(map(int,input().split(' '))) for _ in range(n)]
lst=sorted(lst,key=lambda x : (x[0],x[1],x[2]))

for i in range(n):
    s,e,dist=lst[i][0],lst[i][1],lst[i][2]
    if not (0<=s<d) or not (0<e<=d):
        continue
    if dp[e]-dp[s]>dist:
        for j in range(e,d+1):
            dp[j]=min(dp[j], dp[s]+dist+(j-e))

print(dp[d])
        
