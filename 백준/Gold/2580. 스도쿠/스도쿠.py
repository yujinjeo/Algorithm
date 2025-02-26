import sys

input = sys.stdin.readline

zero = []
board=[]
for i in range(9):
    lst = list(map(int,input().split()))
    for j in range(9):
        if not lst[j]:
            zero.append((i,j))
    board.append(lst)

def rowcheck(x,y,t):
    if t in board[x]:
        return False
    return True

def colcheck(x,y,t):
    for i in range(9):
        if t==board[i][y]:
            return False
    return True

def squarecheck(x,y,t):
    a=x//3
    b=y//3
    for i in range(a*3,a*3+3):
        for j in range(b*3, b*3+3):
            if board[i][j]==t:
                return False
    return True 


def bact(idx):
    global board
    if idx==len(zero):
        for b in board:
            print(*b)
        sys.exit()
        
    x,y = zero[idx][0],zero[idx][1]
    for i in range(1,10):
        if rowcheck(x,y,i) and colcheck(x,y,i) and squarecheck(x,y,i):
            board[x][y]=i
            bact(idx+1)
            board[x][y]=0
    return
    
idx=0
bact(idx)

    