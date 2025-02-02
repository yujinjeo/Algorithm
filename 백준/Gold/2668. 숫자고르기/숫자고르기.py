import sys
import heapq

n=int(input())
board=[0 for _ in range(n+1)]
for i in range(1,n+1):
    board[i]=int(input())
    
visited=[False]*(n+1)
h=[]

for i in range(1,n+1):
    
    if visited[i]:
        continue
    
    s=set()
    s.add(i)
    val=board[i]
    f=False
    
    while True:
        if val==i:
            f=True
            break
        if val in s or visited[val]:
            break
        s.add(val)
        val=board[val]

    if f:
        for j in s:
            visited[j]=True
            heapq.heappush(h,j)
        
            
print(len(h))
while h:
    print(heapq.heappop(h))
