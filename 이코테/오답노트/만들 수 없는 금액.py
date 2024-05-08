import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

target=1
lst.sort()
for i in range(n):
  if target<lst[i]:
    break
  else:
    target+=lst[i]

print(target)
    
