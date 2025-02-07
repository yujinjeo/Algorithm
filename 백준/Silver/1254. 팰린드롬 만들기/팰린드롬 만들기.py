import sys

lst = list(map(str,sys.stdin.readline().rstrip()))

n=len(lst)
stack=[]

def check():
    
    m=len(stack)+n
    if m%2==0:
        l=m//2-1
        r=m//2
    else:
        l=m//2-1
        r=m//2+1

    for i in range(m//2):
        if r>=n:
            if stack[(m-1)-r]!=lst[l]:
                return False
        else:
            if lst[r]!=lst[l]:
                return False
        l-=1
        r+=1
    return True

for i in range(n):
    if check():
        break
    else:
        stack.append(lst[i])

print(n+len(stack))
    
