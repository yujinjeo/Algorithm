import math
import sys

input = sys.stdin.readline
a,b = map(int,input().split())

def net(x):                 
    prime=[True]*(x+1)
    prime[0],prime[1]=False, False
    for i in range(2, int(math.sqrt(x))+1):
        for j in range(2,x//i+1):
            prime[i*j]=False

    return prime

prime=net(int(math.sqrt(b)))

ans=0
for p in range(2,len(prime)):
    if not prime[p]:
        continue
    cand=p
    # print("======", cand)
    
    for i in range(2, 47):
        cand *= p
        if a<=cand:
            ans+=1
        if cand>b:
            ans-=1
            break
        # print(cand, ans)
            
    
print(ans)
