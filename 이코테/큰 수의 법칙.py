# 큰 수의 법칙 (그리디 알고리즘)
import sys
input=sys.stdin.readline

n,m,k=map(int, input().split())
lst=list(map(int, input().split()))

##########나의 풀이
lst.sort(reverse=True)
answer=0
while m>=0:
  if m>=k+1:
    answer+=lst[0]*k + lst[1]*1
    m-=k+1
  else:
    answer+=lst[0]*m
    break

print(answer)

#########이코테 풀이 1
first=lst[0]
second=lst[1]

answer=0
while True:
  if m==0:
    break
  for i in range(k):
    answer+=first
    m-=1
  if m==0:
    break
  answer+=second
  m-=1

print(answer)


#########이코테 풀이 2
first=lst[0]
second=lst[1]

cnt=int(m/(k+1))*k
cnt+=m%(k+1)

answer=0
answer+=cnt*first
answer+=(m-cnt)*second
print(answer)
