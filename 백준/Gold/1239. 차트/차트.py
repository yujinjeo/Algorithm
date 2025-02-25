import sys
from itertools import permutations

input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
lst.sort()

def check(cand):
    cnt=0
    l=len(cand)
    scand=[0 for _ in range(l)]
    scand[0]=cand[0]
    for i in range(1,l):
        scand[i]=scand[i-1]+cand[i]

    for i in range(l):
        if scand[i]+50 in scand:
            cnt+=1
    return cnt

ans=0
for cand in permutations(lst):
    ans=max(ans,check(cand))
print(ans)