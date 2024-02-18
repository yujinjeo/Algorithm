import sys

input=sys.stdin.readline
n=int(input())
answers=[]

for _ in range(n):
  ll=list(map(str,input().strip()))
  if ll==[]:
    print(1)
    continue
  
  tree=[[] for _ in range(26)]
  tree[0].append(0)
  tree[0].append(0)
  
  level=0
  m=0
  for k in ll:
    if k=='[':
      tree[level].pop()
      level+=1
      tree[level].append(1)
      tree[level].append(1)
      if m<level:
        m=level
        
    elif k==']':
      level-=1

  print(2**m)