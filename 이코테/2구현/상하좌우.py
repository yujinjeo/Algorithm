import sys
input=sys.stdin.readline

n=int(input())
lst=list(input().strip().split(' '))
k=len(lst)

x,y=0,0

def move(c):
  global x,y
  if c=='U':
    if y>0:
      y-=1
  elif c=='D':
    if y<n-1:
      y+=1
  elif c=='L':
    if x>0:
      x-=1
  else:
    if x<n-1:
      x+=1
  return
  
for i in range(k):
  move(lst[i])

print(x+1,y+1)
