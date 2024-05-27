import sys
from collections import deque

input = sys.stdin.readline
#dfs인가?
n,m,k,x=map(int,input().split())

nation=[[] for _ in range(n+1)]
cities=[i for i in range(n+1)]
visited=[False for i in range(n+1)]
visited[x]=True

for i in range(m):
  a,b=map(int,input().split())
  nation[a].append(b)
  
# set을 선언할 때는 다음과 같이 선언한다.
answer=set()

q=deque([(k,x)])
while q:
  cnt, city=q.popleft()
  if cnt==0:
    answer.add(city)
    continue
  # q에 넣을 때 visited 처리를 해줘야 다른 곳에서 다시 q에 입력되는 일이 없다.
  for i in range(len(nation[city])):
    if visited[nation[city][i]]==False:
      visited[nation[city][i]]=True
      q.append((cnt-1,nation[city][i]))
    
answer=list(answer)
answer.sort(key=lambda x: x)
if answer==[]:
  print(-1)
else:
  for a in answer:
    print(a)
