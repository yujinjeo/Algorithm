import sys

input = sys.stdin.readline

n,m,k=map(int,input().split(' '))
lst=[]

s,e=2**31,0
for i in range(k):
    a,b=map(int,input().split(' '))
    lst.append((a,b))
    s=min(s,b)
    e=max(e,b)

lst.sort(key=lambda x : -x[0])

# 간 레벨이 x일 때 선호도의 합 m을 채우는 게 가능한가
def check(x):
    sum=0
    cnt=n
    currenti=0
    while True:
        if cnt<=0 or currenti>=k:
            break
        if lst[currenti][1]<=x:
            sum+=lst[currenti][0]
            cnt-=1
        currenti+=1
    if sum>=m and cnt==0:
        return True
    else:
        return False

ans=-1
while s<=e:
    mid=(s+e)//2

    if check(mid):
        ans=mid
        e=mid-1
    else:
        s=mid+1

print(ans)
