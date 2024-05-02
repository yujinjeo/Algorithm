import sys
input=sys.stdin.readline

#### 내 풀이
n,m=map(int, input().split())
lst=[list(map(int,input().split())) for _ in range(n)]

answer=0
for i in range(n):
  cand=min(lst[i])
  if answer<cand:
    answer=cand

print(answer)


#### 이코테 풀이

n,m=map(int,input().split())
answer=0
for i in range(n):
  lst=list(map(int,input().split()))
  cand=min(lst)
  answer=max(answer,cand)

print(answer)
