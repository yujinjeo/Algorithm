import sys
import heapq

input= sys.stdin.readline

n=int(input())
board=[0]+[int(input()) for _ in range(n)]
    
visited=[False]*(n+1)
h=[]

for i in range(1,n+1):
    if visited[i]:
        continue
    s=set()
    s.add(i)
    val=board[i]
    
    while True:
        if val==i:
            for j in s:
                visited[j]=True
                heapq.heappush(h,j)
            break
        if val in s or visited[val]:
            break
        s.add(val)
        val=board[val]
        
            
print(len(h))
while h:
    print(heapq.heappop(h))
