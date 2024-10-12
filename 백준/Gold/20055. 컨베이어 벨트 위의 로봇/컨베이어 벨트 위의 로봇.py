from collections import deque

n,k=map(int,input().split(' '))

a=deque(list(map(int,input().split(' '))))
robot=deque([False for _ in range(n)])
answer=0

while True:
  if a.count(0)>=k:
    break
  answer+=1
  

  a.rotate(1)
  robot[-1]=False
  robot.rotate(1)
  robot[-1]=False

  for i in range(n-2,-1,-1):
    if not robot[i+1] and robot[i] and a[i+1]>0:
      a[i+1]-=1
      robot[i+1],robot[i]=True,False

  if a[0]>0 and robot[0]==False:
    robot[0]=True
    a[0]-=1

  robot[-1]=False

print(answer)