import sys

input = sys.stdin.readline
m,n=map(int,input().split())

lst=list(map(int,input().split()))
lst.sort()

def check(x):
    cnt=0
    for i in range(n-1,-1,-1):
        if x<=lst[i]:
            cnt+=lst[i]//x
        else:
            break
    if cnt>=m:
        return True
    else:
        return False
ans=0
def bin(s,e):
    global ans
    if s>e:
        return
    mid = (s+e)//2
    if check(mid):
        ans=mid
        bin(mid+1,e)
        
    else:
        bin(s,mid-1)

bin(1,lst[-1])
print(ans)



    
