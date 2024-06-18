## 이진탐색으로 풀어보기
import sys

input=sys.stdin.readline
n=int(input())
stock=list(map(int, input().split()))

m=int(input())
order=list(map(int,input().split()))

stock.sort()

answer=[]

def checkstock(o,s,e):
  if s>=e:
    answer.append("no")
    return
  i=(e-s)//2+s
  if stock[i]==o:
    answer.append("yes")
    return
  if stock[i]<o:
    checkstock(o,i+1,e)
  else:
    checkstock(o,s,i)

for i in range(m):
  checkstock(order[i],0,n)

print(*answer)




### SOL2
# 부품 찾기 문제를 이진탐색으로 풀어보자

import sys

input=sys.stdin.readline
n=int(input())
parts=list(map(int, input().split(' ')))
m=int(input())
lst=list(map(int, input().split(' ')))

def bsh(target, start, end):
  middle = (start+end)//2
  if start>end:
    return False
  if parts[middle]==target:
    return True
  elif parts[middle]>target:
    return bsh(target, start,middle-1)
  else:
    return bsh(target,middle+1, end)

answer=["no" for _ in range(m)]

for i in range(m):
  
  if bsh(lst[i],0,n-1):
    answer[i]="yes"

print(*answer)



