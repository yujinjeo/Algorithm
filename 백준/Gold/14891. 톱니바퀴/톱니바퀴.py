import sys
from collections import deque

input =sys.stdin.readline
by=[[]]
for _ in range(4):
  by.append(list(map(str,input().rstrip())))
k=int(input())

def turn(n,d):
  tmp=[]
  for i in range(8):
    tmp.append(by[n][i])
  for i in range(8):
    by[n][i]=tmp[(i-d)%8]

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
    if cand+1<5 and by[cand][2]!=by[cand+1][6] and visited[cand+1]==False:
      q.append((cand+1,-1)) if dir==1 else q.append((cand+1,1))
      turntable.append((cand+1,-1 if dir==1 else 1))
      visited[cand+1]=True
  for i,j in turntable:
    turn(i,j)

print(answer())