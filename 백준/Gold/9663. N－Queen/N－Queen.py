import sys

input = sys.stdin.readline

n=int(input())
ans=0

col=[False]*n

def check(lst, x,y):  
    for i in range(x):
        j=lst[i]
        # 세로 체크
        if j==y: return False
        # 대각선 체크
        cand = abs((i-x)/(j-y))
        if cand==1: return False
        
    return True
        
def bact(lst,cnt):
    global ans, col
    if cnt==n:
        ans+=1
        return
    for i in range(n):
        if not col[i] and check(lst,cnt,i):
            lst.append(i)
            col[i]=True
            bact(lst,cnt+1)
            col[i]=False
            lst.pop()

bact([],0)
print(ans)     