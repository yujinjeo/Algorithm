import sys
import heapq

input=sys.stdin.readline

n,m=map(int,input().split())
board=[[] for _ in range(n+1)]
INF=int(1e9)
dist=[INF]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  board[a].append(b)
  board[b].append(a)

def dijkstra(start):
  dist[start]=0
  q=[]
  heapq.heappush(q,(0,start))
  while q:
    dis,idx=heapq.heappop(q)
    for a in board[idx]:
      if dist[a]>dis+1:
        dist[a]=dis+1
        heapq.heappush(q,(dist[a],a))
  answer_idx=0
  val=0
  cnt=0
  for i in range(1,n+1):
    if val<dist[i]:
      answer_idx=i
      cnt=1
      val=dist[i]
    elif val==dist[i]:
      cnt+=1
  print(answer_idx, val, cnt)

dijkstra(1)
  
