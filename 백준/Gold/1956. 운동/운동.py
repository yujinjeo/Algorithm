import sys

input = sys.stdin.readline

V,E= map(int,input().split())
INF = 1e9
graph = [[INF for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    a,b,c=map(int,input().split())
    graph[a][b]=c

def floyd_warshall(graph):
    for node in range(1,V+1):
        for i in range(1,V+1):
            for j in range(1, V+1):
                if graph[i][j]>graph[i][node]+graph[node][j]:
                    graph[i][j]=graph[i][node]+graph[node][j]

def check():
    ans=INF
    for i in range(1,V+1):
        for j in range(1,V+1):
            ans=min(ans, graph[i][j]+graph[j][i])
    return ans        
    
floyd_warshall(graph)
answer= check()
if answer==INF:
    print(-1)
else:
    print(answer)

