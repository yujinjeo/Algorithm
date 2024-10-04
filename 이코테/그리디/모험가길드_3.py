import sys

input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split(' ')))
lst.sort(reverse=True)
answer=0

k=lst[0]
for i in range(n):
  if k>0:
    k-=1
    continue
  answer+=1
  k=lst[i]

answer+=1
print(answer)

