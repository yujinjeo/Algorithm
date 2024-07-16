import sys

input = sys.stdin.readline

n=int(input())

lst=list(map(int,input().split()))
lst.sort(reverse=True)

i=0
lead=lst[i]
answer=0
while n>i:
  lead=lst[i]
  if i+lead<=n:
    i+=lead
    answer+=1
  else:
    break


print(answer)
    
