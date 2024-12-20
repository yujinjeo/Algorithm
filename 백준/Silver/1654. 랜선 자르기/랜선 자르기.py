import sys

k,n=map(int,input().split(' '))
lst=[0 for _ in range(k)]

for i in range(k):
    lst[i]=int(input())

def check(x):
    cnt=0
    for i in range(k):
        cnt+=lst[i]//x
    if cnt>=n:
        return True
    else:
        return False

ans=0
def binary(s,e):
    global ans
    if s>e:
        return 
    m=(s+e)//2

    ischecked=check(m)
    if not ischecked:
        binary(s,m-1)
    else:
        ans=m
        binary(m+1,e)

start =1
end=max(lst)
binary(start,end)
print(ans)