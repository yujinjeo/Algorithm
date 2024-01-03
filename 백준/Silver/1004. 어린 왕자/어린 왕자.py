import sys
import math

def count_unv():
  x1,y1,x2,y2=map(int, sys.stdin.readline().split())
  n=int(sys.stdin.readline())
  cnt=0

  for i in range(n):
    xc,yc,r=map(int,sys.stdin.readline().split())
    
    len1=math.sqrt(math.pow((x1-xc),2)+math.pow((y1-yc),2))
    len2=math.sqrt(math.pow((x2-xc),2)+math.pow((y2-yc),2))
    if (len1<r and len2>r) or (len1>r and len2<r):
      cnt+=1
  return cnt

t=int(sys.stdin.readline())
ans=[]
for _ in range(t):
  k=count_unv()
  ans.append(k)


for a in ans:
  print(a)
