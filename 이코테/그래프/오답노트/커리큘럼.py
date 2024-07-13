import sys
from collections import deque
import copy

input=sys.stdin.readline

n=int(input())
hours=[0]*(n+1)

graph=[[] for _ in range(n+1)]
topoinput=[0]*(n+1)

for i in range(1,n+1):
  tmp=list(map(int,input().split()))
  hours[i]=tmp[0]
  for j in range(1,len(tmp)):
    if tmp[j]==-1:
      break
    topoinput[i]+=1
    graph[tmp[j]].append(i)

time=copy.deepcopy(hours)
q=deque()

for i in range(1,n+1):
  if topoinput[i]==0:
    q.append(i)

while q:
  idx=q.popleft()
  for i in range(len(graph[idx])):
    # 내가 틀렸던 부분 : 나는 어차피 순서가 정해져 있으니까 계속 더하기를 하면 된다 생각했다. 
    # hours[graph[idx][i]]+=hours[idx]
    # 순서가 정해져있으므로 가장 긴 것을 선택해야 한다. 
    # 반드시 일직선으로 순서가 정해지므로 가장 긴 것을 선택해야 한다. 
    print(graph[idx][i])
    print(hours[idx]+time[graph[idx][i]], hours[graph[idx][i]])
    hours[graph[idx][i]]=max(hours[idx]+time[graph[idx][i]], hours[graph[idx][i]])
    
    topoinput[graph[idx][i]]-=1

    if topoinput[graph[idx][i]]==0:
      q.append(graph[idx][i])

print(hours)
  

