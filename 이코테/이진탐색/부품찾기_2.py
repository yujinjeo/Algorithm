import sys

input =sys.stdin.readline

n=int(input())
items=list(map(int,input().split()))
items.sort()

m=int(input())
lst=list(map(int,input().split()))

def binary_search(target, start, end):
  if start>end:
    return 'no'
  middle=(start+end)//2
  if items[middle]==target:
    return 'yes'
  elif items[middle]>target:
    return binary_search(target,start,middle-1)
  else:
    return binary_search(target,middle+1,end)

answer=[]

for a in lst:
  answer.append(binary_search(a,0,n-1))

print(*answer)
