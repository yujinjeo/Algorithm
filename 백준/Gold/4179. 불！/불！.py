import sys
from collections import deque

input = sys.stdin.readline

r,c=map(int,input().split())
maze = [list(map(str,input().rstrip())) for _ in range(r)]
fired=[[False for _ in range(c)] for _ in range(r)]
visited=[[False for _ in range(c)] for _ in range(r)]
time=0
fire = deque()
jihun=deque()
for i in range(r):
    for j in range(c):
        if maze[i][j]=='F':
            fire.append((i,j,time))
            fired[i][j]=True
        if maze[i][j]=='J':
            jihun.append((i,j,time))
            visited[i][j]=True
            
    
d=[(0,1),(1,0),(0,-1),(-1,0)]
answer=10000

while fire or jihun:
    time+=1

    # 불 번지기
    while fire:
        x,y,check=fire.popleft()
        if check>=time:
            fire.appendleft((x,y,check))
            break
        for dx,dy in d:
            a=x+dx
            b=y+dy
            if 0<=a<r and 0<=b<c and not fired[a][b] and maze[a][b]!='#':
                fire.append((a,b,time))
                fired[a][b]=True
    # 움직이기
    while jihun:
        x,y,check=jihun.popleft()
        if check>=time:
            jihun.append((x,y,check))
            break
        for dx,dy in d:
            a=x+dx
            b=y+dy
            if 0<=a<r and 0<=b<c:
                if not fired[a][b] and not visited[a][b] and maze[a][b]=='.':
                    jihun.append((a,b,time))
                    visited[a][b]=True
            else:
                answer=min(answer, time)

if answer==10000:
    print("IMPOSSIBLE")
else:
    print(answer)
    
    
