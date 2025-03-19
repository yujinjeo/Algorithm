import sys

input = sys.stdin.readline

n,x=map(int,input().split())
lst = list(map(int,input().split()))

maxv=sum(lst[:x])
cand=maxv
cnt=1
for i in range(x,n):
    cand-=lst[i-x]
    cand+=lst[i]
    if cand>maxv:
        maxv=cand
        cnt=1
    elif cand==maxv:
        cnt+=1

if maxv==0:
    print('SAD')
else:
    print(maxv)
    print(cnt)

        