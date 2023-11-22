import sys
n,k=map(int,sys.stdin.readline().split())

list=[i for i in range(n+1)]
list.remove(0)
ans=[0]*n

r=k-1
for i in range(n):
  ans[i]=list.pop(r)
  s=len(list)
  if s!=0:
    r=(r+k-1)%s
  else:
    break

print("<"+", ".join(map(str,ans))+">")