import sys

input = sys.stdin.readline

n,p=map(int,input().split(' '))

# board=[[False for _ in range(p+1)] for _ in range(n+1)]
dic={}
for i in range(1,7):
    dic[i]=set()
    
def minus(order, target):
    cnt=0
    rm=[]
    for i in dic[order]:
        if target<i:
            cnt+=1
            rm.append(i)
    for i in rm:
        dic[order].remove(i)
    return cnt
        
ans=0
for _ in range(n):
    order, pret=map(int,input().split(' '))
    ans+=minus(order, pret)
    if pret not in dic[order]:
        dic[order].add(pret)
        ans+=1
            
print(ans)

