import sys

input = sys.stdin.readline

n=int(input())
lsta=list(map(int,input().split()))

m=int(input())
lstb=list(map(int,input().split()))

def gcb(a,b):
    if a>b:
        while b>0:
            a,b=b,a%b
        return a
    else:
        while a>0:
            b,a=a,b%a
        return b

ans=1

for i in range(n):
    # print("======")
    for j in range(m):
        if lsta[i]==1 or lstb[j]==1:
            continue
        x=gcb(lsta[i],lstb[j])
        if x!=1:
            lsta[i]//=x
            lstb[j]//=x
            ans*=x

# print(lsta)
# print(lstb)

s=str(ans)
if len(s)>9:
    print(s[-9:])
else:
    print(s)
        