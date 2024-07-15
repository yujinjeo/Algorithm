import sys

input=sys.stdin.readline

n,m,k=map(int,input().split())

lst=list(map(int,input().split()))
lst.sort(reverse=True)
first=lst[0]
second=lst[1]


## my sol
i=0
answer=0
while k+1<=m-i:
  answer+=(first*k+second)
  i+=k+1

answer+=first*(m-i)
print(answer)


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

