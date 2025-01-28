import sys
from collections import deque

input =sys.stdin.readline

n,m,k=map(int,input().split(' '))

board=[[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    a,b=map(int,input().split(' '))

    board[a-1][b-1]=1

d=[(0,1),(1,0),(-1,0),(0,-1)]
def bfs(x,y):
    q=deque([(x,y)])
    visited[x][y]=True
    cnt=1
    while q:
        a,b=q.popleft()
        for r in range(4):
            i=a+d[r][0]
            j=b+d[r][1]
            if 0<=i<n and 0<=j<m and board[i][j]==1 and not visited[i][j]:
                visited[i][j]=True
                q.append((i,j))
                cnt+=1
    return cnt

visited=[[False for _ in range(m)] for _ in range(n)]
ans=0
for x in range(n):
    for y in range(m):
        if not visited[x][y] and board[x][y]==1:
            ans=max(ans,bfs(x,y))

print(ans)
            