import sys
sys.setrecursionlimit(10000) 

t=int(input())
ans=[0]*t
ddx=[-1,1,0,0]
ddy=[0,0,1,-1]

def dfs(i,j, graph, visited, n, m):
      visited[i][j]=1
      for k in range(4):
        dx=j+ddx[k]
        dy=i+ddy[k]
        if (0<=dy<n and 0<=dx<m) and (visited[dy][dx]==0 and graph[dy][dx]==1):
            dfs(dy,dx,graph, visited,n,m)


for q in range(t):
    m,n,k=map(int, sys.stdin.readline().split())
    graph=[[0]*m for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    for i in range(k):
        x,y=map(int,sys.stdin.readline().split())
        graph[y][x]=1
        
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and graph[i][j]==1:
                dfs(i,j,graph,visited,n,m)        
                ans[q]+=1
          

for i in ans:
    print(i)
    