from collections import deque

def solution(maps):
    answer = -1
    
    n,m=len(maps),len(maps[0])
    visited=[[False for _ in range(m)] for _ in range(n)]
    
    d=[(0,1),(0,-1),(1,0),(-1,0)]
    
    q=deque([(0,0,1)])
    visited[0][0]=True
    
    while q:
        x,y,cnt=q.popleft()
        
        if x==n-1 and y==m-1:
            answer=cnt
            break
        
        for dx,dy in d:
            a=x+dx
            b=y+dy
            if 0<=a<n and 0<=b<m:
                if maps[a][b]==1 and visited[a][b]==False:
                    visited[a][b]=True
                    q.append((a,b,cnt+1))
    
    return answer
