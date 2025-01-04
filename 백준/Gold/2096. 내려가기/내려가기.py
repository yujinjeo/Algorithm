import sys

input =sys.stdin.readline

n=int(input())

board=list(map(int,input().split(' ')))
min_prev=[board[0],board[1],board[2]]
max_prev=[board[0],board[1],board[2]]

inf=10**9
min_curr=[inf,inf,inf]
max_curr=[0,0,0]

if n==1:
    print(max(board), min(board))
else:
    for i in range(1,n):
        board=list(map(int,input().split(' ')))
        for j in range(3):
            if j in (0,2):
                min_curr[j]=min(min_prev[j], min_prev[(j+1)%2])+board[j]
                max_curr[j]=max(max_prev[j], max_prev[(j+1)%2])+board[j]
            else:
                min_curr[j]=min(min_prev)+board[j]
                max_curr[j]=max(max_prev)+board[j]
                
        min_prev=[min_curr[0],min_curr[1],min_curr[2]]
        max_prev=[max_curr[0],max_curr[1],max_curr[2]]
            
    
    print(max(max_curr),min(min_curr))
