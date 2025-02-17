import sys

input = sys.stdin.readline

while True:
    stack=[]
    lst=list(map(str,input().rstrip()))
    ans=True
    
    if lst[0]=='.':
        break
        
    for i in lst:
        if i== '(':    
            stack.append(True)
        elif i =='[':
            stack.append(False)
        elif i==')':
            if not stack or not stack[-1]:
                ans=False
                break
            else:
                stack.pop()
        elif i==']':
            if not stack or stack[-1]:
                ans=False
                break
            else:
                stack.pop()
    if ans and not stack:
        print('yes')
    else:
        print('no')
    
