import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

lst.sort(reverse=True)
answer=0
i=0
while True:
  if i==n:
    break

  i+=lst[i]
  while i<n:
    if n-i>=lst[i]:
      break
    i+=1
  answer+=1

print(answer)
