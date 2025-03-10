import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
m=int(input())
board=[[0 for _ in range(n+1)] for _ in range(n+1)] 
for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    for j in range(n):
        board[i][j+1]=tmp[j]
    board[i][i]=1
   

for mid in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if not board[i][j]:
                if board[i][mid] and board[mid][j]:
                    board[i][j]=1
                    board[j][i]=1

route = list(map(int,input().split()))

answer='YES'
for i in range(m-1):
    if not board[route[i]][route[i+1]]:
        answer='NO'
        break
print(answer)
