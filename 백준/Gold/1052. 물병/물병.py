import sys

input = sys.stdin.readline
n,k=map(int,input().split())

lst=[]
for i in range(23,-1,-1):
    if 2**i <=n:
        lst.append(2**i)
        n-=2**i

ans=0
if len(lst)<=k:
    print(ans)
else:
    cnt=sum(lst[k:])
    if cnt>=lst[k-1]:
        ans=-1
    else:
        ans=lst[k-1]-cnt
    print(ans)
        

            
        