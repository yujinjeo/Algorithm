import sys

input = sys.stdin.readline

n=int(input())
tmp =[int(input()) for _ in range(n)]
tmp.sort()

lst=[]
for i in range(n-1):
    lst.append(tmp[i+1]-tmp[i])

def gcb(b,a):
    while b>0:
        a,b=b,a%b
    return a

g=lst[0]
for i in range(1,n-1):
    g=gcb(g,lst[i])

ans=set()
for i in range(2, int(g**(1/2))+1):
    if not g%i:
        ans.add(i)
        ans.add(g//i)
ans.add(g)
print(*(sorted(list(ans))))

        