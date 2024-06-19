import sys

input=sys.stdin.readline

n,x=map(int, input().split(' '))
lst = list(map(int, input().split(' ')))



idx1=-1

start=0
end=n-1
while start<=end:
  middle=(start+end)//2
  if lst[middle]>x:
    end=middle-1
  elif lst[middle]==x:
    if (middle>0 and lst[middle-1]<x) or middle==0:
      idx1=middle
      break
    else:
      end=middle-1
  else:
    start=middle+1

###########################################################
idx2=-1

start=0
end=n-1
while start<=end:
  middle=(start+end)//2
  if lst[middle]>x:
    end=middle-1
  elif lst[middle]==x:
    if (middle<n-1 and lst[middle+1]>x) or middle==n-1:
      idx2=middle
      break
    else:
      start=middle+1
  else:
    start=middle+1


if idx1==-1 or idx2==-1:
  print(-1)
else:
  print(idx2-idx1+1)
    
