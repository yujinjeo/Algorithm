import sys


input = sys.stdin.readline
whole=input().rstrip()
dic={
    'H':1,
    'C':12,
    'O':16
}
stack=[]
ans=0
for i in range(len(whole)):
    t=whole[i]
    if t=='(':
        stack.append(t)
    elif t==')':
        c=stack.pop()
        cnt=0
        
        while c!='(':
            cnt+=c
            c=stack.pop()
        stack.append(cnt)

    elif t in dic:
        stack.append(dic[t])
    else:
        stack[-1]*=int(t)

print(sum(stack))