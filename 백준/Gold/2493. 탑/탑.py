import sys
input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
top=[]
for i in range(1,n+1):
    top.append((lst[i-1],i))

stack = []
ans=[0 for _ in range(n)]

for i in range(n):
    cand=top[i][0]
    if not stack:
        stack.append((top[i]))
        continue
    while stack:
        value, index = stack.pop()
        if cand <= value:
            stack.append((top[index-1]))
            ans[i]=index
            break
    stack.append((top[i])) 

print(*ans)