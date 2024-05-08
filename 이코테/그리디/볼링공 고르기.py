import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lst=list(map(int,input().split()))

l=[0 for _ in range(m+1)]


for i in range(n):
  l[lst[i]]+=1

answer=0
for i in range(1,m+1):
  answer+=sum(l[i+1:m+1])*l[i]

print(answer)
