import heapq
import sys

input = sys.stdin.readline
n=int(input())
t=int(input())

lst=list(map(int,input().split(' ')))


cand=[]
heapq.heapify(cand)
current=0

def is_in(x):
    for i in range(current):
        if cand[i][2]==x:
            cand[i][0]+=1
            heapq.heapify(cand)
            return True
    return False

for i in range(t):
    for_x=is_in(lst[i])
    if not for_x:
        if current<n:
            heapq.heappush(cand, [1,i,lst[i]])
            current+=1
        else:
            heapq.heappop(cand)
            heapq.heappush(cand, [1,i,lst[i]])

cand.sort(key=lambda x : (x[2]))
for i in range(current):
    print(cand[i][2], end=' ')  
