import sys

input = sys.stdin.readline

n=int(input())
stack=[0]
ans=[]
cnt=1

for _ in range(n):
    target = int(input())
    while target>stack[-1]:
        stack.append(cnt)
        cnt+=1
        ans.append(True)
    else:
        if target==stack[-1]:
            stack.pop()
            ans.append(False)
        else:
            print('NO')
            sys.exit()
    # print(*stack)
    # print(*ans)

for a in ans:
    if a: print('+')
    else: print('-')
            
            
        
