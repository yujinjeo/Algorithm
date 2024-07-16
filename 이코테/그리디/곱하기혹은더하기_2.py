
import sys

input=sys.stdin.readline

lst=list(map(int,input().rstrip()[:]))

lst.sort()
answer=0

for i in range(len(lst)):
  if lst[i]==0 or lst[i]==1:
    answer+=lst[i]
  else:
    if answer==0:
      answer=1
    answer*=lst[i]

print(answer)
