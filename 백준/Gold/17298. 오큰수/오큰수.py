import sys

input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

stack=[]
temp=[]

ans=[-1 for _ in range(n)]

for i in range(n-1,-1,-1):
    cur=lst[i]
    if not stack:
        stack.append(cur)
        continue
    
    while stack:
        top=stack.pop()
        if top<=cur:
            temp.append(top)
        else:
            ans[i]=top
            stack.append(top)
            break
            
    if ans[i]==-1:
        while temp:
            top=temp.pop()
            if top>cur:
                ans[i]=top
                stack.append(top)
            else:
                temp.append(top)
                break
                
    stack.append(cur)
        

print(*ans)
            

