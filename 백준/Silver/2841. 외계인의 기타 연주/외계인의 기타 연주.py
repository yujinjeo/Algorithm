import sys

input = sys.stdin.readline

n,p=map(int,input().split(' '))

# board=[[False for _ in range(p+1)] for _ in range(n+1)]
dic={}
for i in range(1,7):
    dic[i]=[]
    
def minus(order, target):
    cnt=0
    l=len(dic[order])
    for i in range(l-1,-1,-1):
        if target<dic[order][i]:
            dic[order].remove(dic[order][i])
            cnt+=1
        else:
            break 
    return cnt
        
ans=0
for _ in range(n):
    order, pret=map(int,input().split(' '))
    ans+=minus(order, pret)
    if pret not in dic[order]:
        dic[order].append(pret)
        ans+=1
            
print(ans)

