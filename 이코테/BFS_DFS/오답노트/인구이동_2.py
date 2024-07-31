import sys
from collections import deque

input = sys.stdin.readline
n,r,c=map(int,input().split(' '))
board=[list(map(int, input().split())) for _ in range(n)]
d=[(0,1),(1,0),(-1,0),(0,-1)]

def bfs(o,k,cand):
  lst=[(o,k)]
  q=deque()
  q.append((o,k))
  while q:
    x,y=q.popleft()
    for dx, dy in d:
      a=x+dx
      b=y+dy
      if 0<=a<n and 0<=b<n and visited[a][b]==False:
        if r<=abs(cand[x][y]-cand[a][b])<=c:
          q.append((a,b))
          lst.append((a,b))
          visited[a][b]=True
  if len(lst)==1:
    return False
  sum=0 
  for x,y in lst:
    sum+=cand[x][y]
  val=sum//len(lst)
  for x,y in lst:
    cand[x][y]=val
  return True

answer=0

# 이런 식으로 board 전체를 섬 구석구석 점검한다. visited으로 설정 후 계속 반복 
# visited로 구역을 구분해준다. visited를 사용하면 list의 list를 저장하지 않고도 구역 사용이 가능하다.
while True:
  is_change=False
  visited=[[False for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if visited[i][j]==False:
        visited[i][j]=True
        val= bfs(i,j,board)
        if val==True:
          is_change=True
  if is_change:
    answer+=1
  else:
    break

print(answer)
