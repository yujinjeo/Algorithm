import sys

input = sys.stdin.readline

n,m=map(int,input().split(' '))
lst=[int(input()) for _ in range(m)]

def check(x):
    cnt=0
    for color in lst:
        if color<=x:
            cnt+=1
            continue
        if color%x==0:
            cnt+=color//x
        else:
            cnt+=color//x+1

    if cnt<=n:
        return True
    else:
        return False

s,e=1,max(lst)
ans=e
while s<=e:
    mid=(s+e)//2
    if check(mid):
        ans=mid
        e=mid-1
    else:
        s=mid+1

print(ans)
        
    

