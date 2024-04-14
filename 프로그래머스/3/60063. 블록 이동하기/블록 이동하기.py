from collections import deque
d=[[0,1],[0,-1],[1,0],[-1,0]]

def move(l1,l2, n, board):
    cand=[]
    x1,y1=l1
    x2,y2=l2
    #상하좌우
    for i in range(4):
        a1=x1+d[i][0]
        a2=x2+d[i][0]
        b1=y1+d[i][1]
        b2=y2+d[i][1]
        if board[a1][b1]==0 and board[a2][b2]==0:
            cand.append(((a1,b1),(a2,b2)))
    #가로일 때
    if x1==x2:
        for i in [-1,1]:
            if board[x1+i][y1]==0 and board[x2+i][y2]==0:
                cand.append(((x1,y1),(x1+i,y1)))
                cand.append(((x2,y2),(x2+i,y2)))
    else:
        for i in [-1,1]:
            if board[x1][y1+i]==0 and board[x2][y2+i]==0:
                cand.append(((x1,y1+i),(x1,y1)))
                cand.append(((x2,y2+i),(x2,y2)))
    return cand


def solution(_board):
    
    n=len(_board)
    
    board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            board[i+1][j+1] = _board[i][j]
    
    visited=set([((1,1),(1,2))])
    q=deque([((1,1),(1,2),0)])
    
    while q:
        l1,l2,cnt=q.popleft()
        if (l1[0]==n and l1[1]==n) or (l2[0]==n and l2[1]==n):
            return cnt
        cand = move(l1,l2,n, board)
        for can in cand:
            if can not in visited:
                visited.add(can)
                q.append((*can, cnt+1))
