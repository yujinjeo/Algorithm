import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int, input().split())
board=[[] for i in range(n+1)]
ans=[]

# 트리 정보 입력받기
for i in range(n-1):
  s,e,w=map(int,input().split())
  board[s].append((e,w))
  board[e].append((s,w))
  
# 거리를 알고 싶은 두 정점 입력받기
for _ in range(m):
  s,e=map(int,input().split())
  q=deque()
  q.append((s,0))
  visited=[False]*(n+1)

  while q:
    node, dist=q.popleft()
    
    if node==e:
      ans.append(dist)
      break
    
    for j,w in board[node]:
      if visited[j]==False:
        q.append((j,dist+w))
        visited[j]=True

        
#한 줄에 정답 하나씩 출력
for a in ans:
  print(a)