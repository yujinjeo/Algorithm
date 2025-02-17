import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
lst= list(map(int,input().split()))
q=deque(lst)

stack=[n+1]

for turn in range(1,n+1):
    
    # 1. 확인
    if q and q[0]==turn:
        q.popleft()
        continue
    if stack[-1]==turn:
        stack.pop()
        continue
        
    check=False
    
    while q:
        cand=q.popleft()
        if cand!=turn:
            if stack[-1]>q[0]:
                stack.append(cand)
            else:
                print("Sad")
                sys.exit()
        else:
            check=True
            break
            
    if not check:
        if stack[-1]!=turn:
            print("Sad")
            sys.exit()
        else:
            stack.pop()

print("Nice")
