import sys

input=sys.stdin.readline

n=int(input())
parent=[-2]*(n+1)
child=[False]*(n+1)
child[0]=True
ans=[-2]*(n+1)

for i in range(n):
  parent[i+1]=int(input())

while True:
  if False not in child:
    break
  for c in range(1,n+1):
    if child[c]==False:
      if parent[c]==-1:
        ans[c]=0
        child[c]=True
      elif ans[parent[c]]!=-2:
        ans[c]=ans[parent[c]]+1
        child[c]=True

for a in range(1,n+1):
  print(ans[a])