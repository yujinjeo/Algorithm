import sys

input = sys.stdin.readline

n,m = map(int,input().split(' '))
lst=['' for _ in range(n)]
alpha=0

for i in range(n):
  lst[i]=input().rstrip()
  alpha+=len(lst[i])

small = (m-alpha)//(n-1) 
big=small+1 
bs = (m-alpha -n*small + small)//(big-small)
ss=(n-1)-bs

answer=lst[0]
for i in range(1,n):
  if lst[i][0]>='a':
    if bs>0:
      bs-=1
      answer+='_'*big
    else:
      ss-=1
      answer+='_'*small
  else:
    if ss>0:
      ss-=1
      answer+='_'*small
    else:
      bs-=1
      answer+='_'*big
  answer+=lst[i]   

print(answer)


