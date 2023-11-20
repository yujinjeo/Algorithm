import sys

#기본정보 입력받기
n,m,v=map(int, sys.stdin.readline().split())

#이런 간선과 정점으로 이루어진 정보는 행렬을 만들어 데이터화 할 수 있다.
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a][b]=graph[b][a]=1

#visited이라는 리스트를 만들어서 따로 관리할 수 있다.
visited1=[0]*(n+1)
visited2=visited1.copy()

#dfs는 stack이다. 계속 깊게 파고드는. 재귀함수를 만들면 됨.
def dfs(v):
    visited1[v]=1
    print(v,end=' ')
  #정점 v의 행을 둘러보면서 가장 먼저 찾는 정점으로 들어간다.
    for i in range(1,n+1):
        if visited1[i]==0 and graph[v][i]==1:
            dfs(i)

def bfs(v):
    queue=[v]
    visited2[v]=1
    while queue:
        p=queue.pop(0)
        print(p,end=' ')
        for i in range(1,n+1):
            if visited2[i]==0 and graph[p][i]==1:
                queue.append(i)
                visited2[i]=1


dfs(v)
print()
bfs(v)