# sol 1 :함수 풀이

import sys

input =sys.stdin.readline

n,k=map(int,input().split())

lst=list(map(int,input().split()))

start_idx=n
end_idx=-1

def binary_search(target,start,end):

  global start_idx, end_idx
  
  if start>end:
    return -1
  mid=(start+end)//2
  val=lst[mid]

  if target==val:
    start_idx=min(start_idx,mid)
    end_idx=max(end_idx,mid)
    binary_search(target,start,mid-1)
    binary_search(target,mid+1,end)
  elif target>val:
    binary_search(target,mid+1,end)
  else:
    binary_search(target,start,mid-1)



binary_search(k,0,n-1)

if start_idx==n or end_idx==-1:
  print(-1)
else:
  print(end_idx-start_idx+1)
  
# sol 2 : python 내장함수 bisect_left, bisect_right 사용

import sys
from bisect import bisect_left, bisect_right

input=sys.stdin.readline

n,k=map(int,input().split())
lst=list(map(int, input().split()))

# bisect_left : target이상의 수 중 가장 작은 index 반환
start_idx= bisect_left(lst,k)
# bisect_right : target 초과의 수 중 가장 작은 index 반환
end_idx= bisect_right(lst,k)

cnt=end_idx-start_idx
if cnt==0:
  print(-1)
else:
  print(cnt)
