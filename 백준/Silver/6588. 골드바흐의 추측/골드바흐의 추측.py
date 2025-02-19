import sys
input = sys.stdin.readline

def net(x):
    board=[True for i in range(x+1)]
    board[0], board[1], board[2]=False, False, False
    for i in range(3,x//2+1):
        if not board[i]: continue
        for j in range(2, x//i+1):
            if board[i*j]:
                board[i*j]=False
    return board
    
maxv=-1
lst=[]
while True:
    n=int(input())
    if not n: break
    maxv=max(maxv, n)
    lst.append(n)

prime=net(maxv)

for i in range(len(lst)):
    n=lst[i]
    for j in range(3,n,2):
        if prime[j] and prime[n-j]:
            print(n,"=",j,"+",n-j)
            break
    

    
