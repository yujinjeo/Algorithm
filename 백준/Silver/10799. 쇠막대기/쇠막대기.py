import sys

input = sys.stdin.readline
lst = list(map(str,input().rstrip()))
n=len(lst)
stack=[]
s=0
ans=0
before=False
for i in range(n):
    if lst[i]=='(':
        stack.append(s)
        s+=1
        before=True
    else:
        if before:
            ans+=stack.pop()
            s-=1
        else:
            ans+=1
            s-=1
        before=False

print(ans)

