import sys

input=sys.stdin.readline

n,m=map(int,input().split())

answer=0
for _ in range(n):
  lst=list(map(int,input().split()))
  val=min(lst)
  answer=max(answer,val)


print(answer)
