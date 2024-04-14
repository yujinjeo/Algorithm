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
        if 0<=a1<n and 0<=a2<n and 0<=b1<n and 0<=b2<n:
            if board[a1][b1]==0 and board[a2][b2]==0:
                cand.append(((a1,b1),(a2,b2)))
    #가로일 때
    if x1==x2:
        for i in [-1,1]:
            if 0<=x1+i<n and 0<=x2+i<n:
                if board[x1+i][y1]==0 and board[x2+i][y2]==0:
                    cand.append(((x1,y1),(x1+i,y1)))
                    cand.append(((x2,y2),(x2+i,y2)))
    else:
        for i in [-1,1]:
            if 0<=y1+i<n and 0<=y2+i<n:
                if board[x1][y1+i]==0 and board[x2][y2+i]==0:
                    cand.append(((x1,y1+i),(x1,y1)))
                    cand.append(((x2,y2+i),(x2,y2)))
    return cand

#이 문제는 최소거리를 찾는 BFS 알고리즘을 잘 기억하고 있다면 응용해서 풀 수 있습니다.
# 0과 1로 이루어진 board에서 1,1 부터 n,n 까지 최소거리를 구하는 방법은,
# 상하좌우로 움직인 다음, visited에 없고, 움직일 수 있다면 cnt와 함께 q에 넣고, q에서 n,n 이 나오면 멈추고 cnt를 반환하는 방식입니다.
# 이 문제도, 움직이는 것은 상하좌우, 회전까지 포함하고,
# visitied에 넣을 것은 똑같이 로봇이 방문한 좌표인 것입니다. 
# 기본 문제와 알고리즘 자체는 거의 100% 똑같다고 볼 수 있습니다.
    
# 추가적으로, {(0,0),(a,a)} 튜플을 이런 식으로 사용하면 {(n,n),(0,0)} 과 같은 set으로 인식한다는 것,
# 그리고 회전할 때, 가로- 4경우, 세로 -4 경우 이렇게 다 확인할 필요 없이, if board[x1+i][y1]==0 and board[x2+i][y2]==0: 이런 식으로, 가로일 때 세로로 세우고 싶으면
# 한 쪽만 세울 수 있어도 양쪽 다 세울 수 있다는 것을 활용하여 간단하게 경우의 수를 구분할 수 있습니다. 이런 아이디어는 쉽게 떠오르지는 않겠지만, 기본적으로 경우의 수를 
# 잘 나누는 것부터가 이런 아이디어의 시작이 될 것 같습니다. 
# 그리고, 주위에 1로 외벽을 세워서, move 함수에서 범위를 확인하지 않아도 되도록 만들 수 있다는 것도 배울 수 있었습니다.

def solution(board):
    
    n=len(board)
    visited=set([((0,0),(0,1))])
    q=deque([((0,0),(0,1),0)])
    
    while q:
        l1,l2,cnt=q.popleft()
        if (l1[0]==n-1 and l1[1]==n-1) or (l2[0]==n-1 and l2[1]==n-1):
            return cnt
        cand = move(l1,l2,n, board)
        for can in cand:
            if can not in visited:
                visited.add(can)
                q.append((*can, cnt+1))
