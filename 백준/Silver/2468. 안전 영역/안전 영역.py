import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
board=[[] for _ in range(n)]
minv=10**9
maxv=0
for i in range(n):
    lst=list(map(int,input().split(' ')))
    minv=min(minv,min(lst))
    maxv=max(maxv,max(lst))
    board[i]=lst
    
d=[(0,1),(1,0),(0,-1),(-1,0)]
def bfs(i,j, height):
    q=deque([(i,j)])
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            a=x+dx
            b=y+dy
            if 0<=a<n and 0<=b<n and not visited[a][b]:
                if board[a][b] > height:
                    q.append((a,b))
                    visited[a][b]=True

ans=0
for height in range(minv-1, maxv):
    visited=[[False for _ in range(n)] for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j]>height:
                visited[i][j]=True
                bfs(i,j,height)
                cnt+=1
    ans=max(ans, cnt)

print(ans)

