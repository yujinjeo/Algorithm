import sys

input = sys.stdin.readline
a,b = map(int,input().split())

def net(x):                 
    prime=[True]*(x+1)
    prime[0],prime[1]=False, False
    for i in range(2, int(x**0.5)+1):
        for j in range(2,x//i+1):
            prime[i*j]=False

    return prime

prime=net(int(b**0.5))

ans=0
cand=2
for i in range(2,47):
    cand *= 2
    if a<=cand:
        ans+=1
    if cand>b:
        ans-=1
        break


for p in range(3,len(prime),2):
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
