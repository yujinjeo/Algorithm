import sys

input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

def bisect(start, end):
  if start>end:
    return -1
  mid=(start+end)//2

  if lst[mid]==mid:
    return mid
  elif lst[mid]>mid:
    return bisect(start,mid-1)
  else:
    return bisect(mid+1,end)

print(bisect(0,n-1))


