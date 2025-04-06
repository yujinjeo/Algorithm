import sys

input = sys.stdin.readline

n, b=map(int,input().split())

matrix=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j]%=1000

def multiplex(U,V):
    ans=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cand=0
            for k in range(n):
                cand+=U[i][k]*V[k][j]
            ans[i][j]=cand%1000
    return ans

def func(board, cnt):
    if cnt==1:
        return matrix
        
    a=func(board, cnt//2)
    
    if cnt%2:
        return multiplex(multiplex(a,a), matrix)
    else:
        return multiplex(a,a)

answer=func(matrix, b)
for i in range(n):
    print(*answer[i])
    