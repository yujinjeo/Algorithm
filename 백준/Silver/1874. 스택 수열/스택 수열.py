import sys

input =sys.stdin.readline

n=int(input())

lst=[int(input()) for _ in range(n)]
stack=[0]
ans=[]
maxv=0

for i in range(n):
    target=lst[i]
    top=stack[-1]

    if top==target:
        ans.append('-')
        stack.pop()
        continue
    
    if target<top:
        cand=stack.pop()
        if cand!=target:
            print('NO')
            sys.exit()
        ans.append('-')
    else:
        for j in range(maxv+1,target):
            stack.append(j)
            ans.append("+")
        maxv=max(maxv,target)
        ans.append("+")
        ans.append('-') 
    # print(target, stack)
for a in ans:
    print(a)
            

