import sys
import heapq

input = sys.stdin.readline

n=int(input())

h=[]
for _ in range(n):
    h.append(tuple(map(int,input().split(' '))))

h.sort(key=lambda x : (x[0],-x[1]))

start,end=h[0][0],h[0][1]
ans=0

for i in range(1,n):
    s,e=h[i][0],h[i][1]
    if start==s:
        continue
    elif s<end:
        end=max(end,e)
    else:
        ans+=end-start
        start,end=s,e

print(ans+(end-start))


