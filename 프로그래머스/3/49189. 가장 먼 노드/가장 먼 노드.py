from collections import deque

def solution(n, edge):
    answer = 1
    numbers=[]
    q=deque()
    graph=[[] for _ in range(n+1)]
    visited=[False for _ in range(n+1)] 
    visited[1]=True
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        if a==1:
            q.append((b,answer+1))
            visited[b]=True
        if b==1:
            q.append((a,answer+1))
            visited[a]=True
        
    
    while q:
        target,cnt=q.popleft()
        print(target, cnt)
        for a in graph[target]:
            if visited[a]==False:
                visited[a]=True
                q.append((a,cnt+1))
        answer=max(answer,cnt)
        numbers.append(cnt)

    return numbers.count(answer)

