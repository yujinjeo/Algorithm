
# 백준 14891번 2024-10-10

import sys
from collections import deque

input =sys.stdin.readline
by=[[]]
for _ in range(4):
  by.append(list(map(str,input().rstrip())))
k=int(input())

def turn(m,y):
  tmp=[]
  for i in range(8):
    tmp.append(by[m][i])
  for i in range(8):
    # tmp의 값을 by에 옮기는 것이므로 +y 가 아니라 -y 로 계산되어야 한다.
    by[m][i]=tmp[(i-y)%8]

def answer():
  answer=0
  if by[1][0]=='1':
    answer+=1
  if by[2][0]=='1':
    answer+=2
  if by[3][0]=='1':
    answer+=4
  if by[4][0]=='1':
    answer+=8
  return answer
    
for _ in range(k):
  n,d=map(int,input().split(' '))
  q=deque([(n,d)])
  turntable=[(n,d)]
  visited=[False for i in range(5)]
  visited[n]=True
  while q:
    cand,dir=q.popleft()
    if cand-1>0 and by[cand][6]!=by[cand-1][2] and visited[cand-1]==False:
      q.append((cand-1,-1)) if dir==1 else q.append((cand-1,1))
      turntable.append((cand-1,-1 if dir==1 else 1))
      visited[cand-1]=True
    # elif 가 아니라 if 로 계산해야 양쪽 다 탐색을 할 수 있게 된다.
    if cand+1<5 and by[cand][2]!=by[cand+1][6] and visited[cand+1]==False:
      # 그리고 여기 변수를... dir 가 아니라 d 로 적었다. 변수가 많을 경우 변수를 잘 적었는지도 확인하자.
      q.append((cand+1,-1)) if dir==1 else q.append((cand+1,1))
      turntable.append((cand+1,-1 if dir==1 else 1))
      visited[cand+1]=True
  for i,j in turntable:
    turn(i,j)

print(answer())
