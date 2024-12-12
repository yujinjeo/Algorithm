import sys
from collections import deque

input = sys.stdin.readline

n=int(input())
lst = list(map(int,input().rstrip().split(' ')))
a,b = map(int, input().split(' '))
visited=[False]*n

q=deque([(a-1,0)])
visited[a-1]=True

answer=-1

while q:
  current,jump=q.popleft()
  if current==b-1:
    answer=jump
    break

  value=lst[current]
  tol=1
  # 왼쪽으로 가기 
  while current-value*tol>=0:
    if not visited[current-value*tol]:
      q.append((current-value*tol,jump+1))
      visited[current-value*tol]=True
    tol+=1
  # 오른쪽 탐색
  tor=1
  while current+value*tor<n:
    if not visited[current+value*tor]:
      q.append((current+value*tor, jump+1))
      visited[current+value*tor]=True
    tor+=1

print(answer)
