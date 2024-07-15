import sys

input=sys.stdin.readline

n,m,k=map(int,input().split())

lst=list(map(int,input().split()))
lst.sort(reverse=True)
first=lst[0]
second=lst[1]


## my sol
# i=0
# answer=0
# while k+1<=m-i:
#   answer+=(first*k+second)
#   i+=k+1

# answer+=first*(m-i)
# print(answer)


## 나의 풀이를 더 간단하게 만드는 방법
# 왜? 일정한 수만큼 반복되기 때문에, 이런 식으로 count 횟수를 미리 파악할 수 있다.
# first를 더하는 횟수
count = int(m/(k+1))*k+m%(k+1)
answer=count*first
answer+=(m-count)*second


## book's sol

# answer2=0
# while True:
#   for _ in range(k):
#     if m==0:
#       break
#     answer2+=first
#     m-=1
#   if m==0:
#     break
#   answer2+=second
#   m-=1

# print(answer2)

