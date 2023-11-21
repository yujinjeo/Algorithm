import sys
from collections import deque

#명령 종류를 리스트화 해서 관리한다
command=["push", "pop", "size", "empty", "top"]
ans=[]
queue=deque()
n=int(input())

for _ in range(n):
  cmd=list(sys.stdin.readline().split())
  
  if cmd[0]==command[0]:
    queue.append(int(cmd[1]))
    
  elif cmd[0]==command[1]:
    if len(queue)==0:
      a=-1
    else:
      a=queue.pop()
    ans.append(a)
    
  elif cmd[0]==command[2]:
    a=queue.__len__()
    ans.append(a)
    
  elif cmd[0]==command[3]:
    if len(queue)==0:
      a=1
    else:
      a=0
    ans.append(a)
    
  else:
    if len(queue)==0:
      a=-1
    else:
      a=queue[-1]
    ans.append(a)
        
  
for a in ans:
  print(a)