from collections import deque

t=int(input())

def bfs():
  q=deque()
  q.append((x,y))

  while q:
    i,j=q.popleft()
    #도착지에 도달할 수 있는지 확인
    dist=abs(a-i)+abs(b-j)
    if dist<=1000:
      print("happy")
      return

    for r in range(con):
      if visited[r]!=1:
        cx,cy=stores[r]
        temp=abs(cx-i)+abs(cy-j)
        if temp<=1000:
          visited[r]=1
          q.append((cx,cy))

  print("sad")
  return

ans=[]
for _ in range(t):
  #편의점의 개수
  con=int(input())
  #상근이네 집 좌표
  x,y=map(int,input().split())

  #편의점 좌표 받기
  stores=[]
  visited=[0 for _ in range(con)]
  for i in range(con):
    i,j=map(int,input().split())
    stores.append((i,j))

  #페스티벌 좌표
  a,b=map(int,input().split())

  bfs()