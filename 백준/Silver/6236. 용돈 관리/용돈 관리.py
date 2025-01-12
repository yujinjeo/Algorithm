import sys
input=sys.stdin.readline

n,m=map(int,input().split(' '))

lst=[0 for _ in range(n)]

for i in range(n):
    lst[i]=int(input())

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

ans=0
def bin(s,e):
    global ans
    if s>e:
        return 

    m=(s+e)//2
    if check(m):
        ans=m
        bin(s,m-1)
    else:
        bin(m+1,e)

bin(min(lst),sum(lst))
print(ans)
        

