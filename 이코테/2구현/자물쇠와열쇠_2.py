from copy import deepcopy

def turnright(key):
    m=len(key)
    key2=deepcopy(key)
    for i in range(m):
        for j in range(m):
            key[i][j]=key2[m-1-j][i]
    

def checkok(board,n,m):
    for i in range(n):
        for j in range(n):
            if board[i+m-1][j+m-1]!=1:
                return False
    return True
    
def solution(key, lock):
    answer = True
    m=len(key)
    n=len(lock)
    board=[[0 for _ in range(n+2*m-2)] for _ in range(n+2*m-2)]
    for i in range(n):
        for j in range(n):
            board[i+m-1][j+m-1]=lock[i][j]
                
    for _ in range(4):
        turnright(key)
        
        for i in range(n+m-1):
            for j in range(n+m-1):
                board2=deepcopy(board)
                for r in range(m):
                    for w in range(m):
                        board2[i+r][j+w]+=key[r][w]      
                if checkok(board2,n,m):
                    print
                    return True

    return False
