import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()

indexof=[0 for _ in range(m)]

for i in range(1,m+1):
  indexof[i-1]=lst.index(i)

answer=0
for i in range(m-1):
  count=indexof[i+1]-indexof[i]
  answer+=count*(n-indexof[i+1])

print(answer)
  
