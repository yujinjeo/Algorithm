import sys

input=sys.stdin.readline

n,m=map(int,input().split(' '))

lst=[int(input()) for _ in range(n)]

def check(x):
    cnt=1
    current=x
    for i in range(n):
        if x<lst[i]:
            return False
        if current>=lst[i]:
            current-=lst[i]
        else:
            current=x-lst[i]
            cnt+=1
    if cnt<=m:
        return True
    else:
        return False

s=min(lst)
e=sum(lst)
while s<=e:
    mid=(s+e)//2
    if check(mid):
        ans=mid
        e=mid-1
    else:
        s=mid+1

print(ans)