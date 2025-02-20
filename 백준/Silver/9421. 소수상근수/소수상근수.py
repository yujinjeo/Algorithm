import sys

input = sys.stdin.readline

def net(n):
    board=[True for _ in range(n+1)]
    prime=[]
    
    for i in range(2, n//2+1):
        for j in range(2, n//i+1):
            board[i*j]=False
        if board[i]:
            prime.append(i)
    for i in range(n//2+1, n+1):
        if board[i]:
            prime.append(i)
    return prime

def cal(x):
    ans=0
    s=str(x)
    for i in s:
        ans+=(int(i))**2
    return ans

def check(x):
    # print(x, "=======")
    prev=set()
    while True:
        # print(prev)
        cand = cal(x)
        if cand==1:
            return True
        if cand not in prev:
            prev.add(cand)
            x=cand
        else:
            return False   
    return False    

n = int(input())
prime=net(n)

for p in prime:
    if check(p):
        print(p)
