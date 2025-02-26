import sys
input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
lst.sort()

anss, anse=0,0

def check(x):
    global anss, anse
    s,e=0,n-1
    while True:
        if s>=e:
            return False
        cand=lst[s]+lst[e]
        if abs(cand)<=x:
            anss,anse = lst[s],lst[e]
            return True
        if cand>0:
            e-=1
        else:
            s+=1
    return False

ans=0
def bin(s,e):
    if s>e:
        return
    mid = (s+e)//2

    if check(mid):
        bin(s,mid-1)
    else:
        bin(mid+1,e)

bin(0,abs(lst[0]+lst[-1]))
print(anss, anse)

        
        
            