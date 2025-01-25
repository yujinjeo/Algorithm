import sys
input = sys.stdin.readline
n=int(input())
s=input().rstrip()

stack=[]
stack.append((s[0],1))

ans=0

for i in range(1,n):
    if len(stack)==0:
        stack.append((s[i],1))
        continue
        
    if stack[-1][0]!=s[i][0]:
        t,c=stack.pop()
        ans=max(ans,c)
    else:
        stack.append((s[i],stack[-1][1]+1))
    

if len(stack)==0:
    print(ans)
else:
    print(-1)