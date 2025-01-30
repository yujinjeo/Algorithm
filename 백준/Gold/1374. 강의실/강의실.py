import sys
import heapq
input =sys.stdin.readline

n=int(input())

l=[list(map(int,input().split(' '))) for _ in range(n)]
l.sort(key=lambda x : x[1])

room=[0]
for i in range(n):
    start,end=l[i][1],l[i][2]
    k= heapq.heappop(room)
    if k>start:
        heapq.heappush(room,k)
    heapq.heappush(room,end)
    # print(room)

print(len(room))

