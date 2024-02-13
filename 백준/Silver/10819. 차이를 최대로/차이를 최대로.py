import sys

input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

#백트래킹 순열
max_val=0

def bact(cnt):
  global max_val
  if cnt==n:
    value=0
    for i in range(0,n-1):
      value+=abs(picked[i]-picked[i+1])
    if max_val<value:
      max_val=value
    return
  for i in range(n):
    if visited[i]==False:
      picked.append(lst[i])
      visited[i]=True
      bact(cnt+1)
      picked.pop()
      visited[i]=False

for i in range(n):
  picked=[lst[i]]
  visited=[False]*(n)
  visited[i]=True
  bact(1)

print(max_val)