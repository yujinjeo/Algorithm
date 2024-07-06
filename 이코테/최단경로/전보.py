import sys
import heapq

input=sys.stdin.readline

n,m,c=map(int,input().split())

board=[[] for i in range(n+1)]
INF=int(1e9)
distance=[INF]*(n+1)

for i in range(m):
  a,b,e=map(int,input().split())
  board[a].append((b,e))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0

  while q:
    dis,idx=heapq.heappop(q)
    if distance[idx]<dis:
      continue
    for i in board[idx]:
      if distance[i[0]]>dis+i[1]:
        distance[i[0]]=dis+i[1]
        heapq.heappush(q,(distance[i[0]],i[0]))

dijkstra(c)

cnt=0
maxval=0
for i in range(1,n+1):
  if distance[i]==INF or i==c:
    continue
  else:
    cnt+=1
    maxval=max(maxval, distance[i])

print(cnt, maxval)

