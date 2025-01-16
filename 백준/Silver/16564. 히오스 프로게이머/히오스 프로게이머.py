import sys

input = sys.stdin.readline

n,k=map(int,input().split(' '))

lst=[int(input()) for _ in range(n)]
lst.sort()

# x 는 최소 레벨 후보
def check(x):
    cnt=0
    for i in range(n):
        if lst[i]>=x:
            break
        else:
            cnt+=x-lst[i]
    if cnt>k:
        return False
    else:
        return True

s=lst[0]
e=lst[-1]+k
ans=0
while s<=e:
    mid=(s+e)//2
    if check(mid):
        s=mid+1
        ans=mid
    else:
        e=mid-1

print(ans)
        
