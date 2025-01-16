from collections import deque

d=[(0,1),(0,-1),(-1,0),(1,0)]

n,m=map(int,input().split(' '))

board=[list(map(int,input().split(' '))) for _ in range(n)]

def bfs(i,j):
    q=deque([(i,j)])
    cnt=1
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            a=x+dx
            b=y+dy
            if 0<=a<n and 0<=b<m and not visited[a][b] and board[a][b]==1:
                q.append((a,b))
                visited[a][b]=True
                cnt+=1

    
    return cnt
    
q=deque()
visited=[[False for _ in range(m)] for _ in range(n)]
ans=0
maxw=0

for i in range(n):
    for j in range(m):
        if board[i][j]==1 and not visited[i][j]:        
            visited[i][j]=True
            maxw=max(maxw,bfs(i,j))
            ans+=1

print(ans)
print(maxw)
        

    
