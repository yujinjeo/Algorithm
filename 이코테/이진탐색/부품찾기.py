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
