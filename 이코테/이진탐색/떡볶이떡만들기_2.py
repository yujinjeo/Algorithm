import sys

input =sys.stdin.readline

n,m=map(int,input().split())
lst=list(map(int, input().split()))

minval=0

def isok(cand):
  answer=0
  for i in range(len(lst)):
    if lst[i]<cand:
      continue
    answer+=lst[i]-cand
  return answer

def binary_search(target, start,end):
  global minval
  if start>end:
    return
  mid=(start+end)//2
  val=isok(mid)
  if val==target:
    minval=max(minval,mid)
  elif val<target:
    binary_search(target,start,mid-1)
  else:
    minval=max(minval,mid)
    binary_search(target,mid+1, end)

binary_search(m, 0, max(lst))
print(minval)
