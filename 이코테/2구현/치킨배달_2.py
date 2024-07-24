import sys

input = sys.stdin.readline

n,m=map(int, input().split())
board=[list(map(int, input().split()))for _ in range(n)]
home=[]
chicken=[]
for i in range(n):
  for j in range(n):
    if board[i][j]==1:
      home.append((i,j))
    elif board[i][j]==2:
      chicken.append((i,j))


visited=[False]*(len(chicken))
answers=[]

def findMinVal():
  answer=0
  for i in range(len(home)):
    x,y=home[i]
    cand=1e9
    for j in range(len(visited)):
      if visited[j]==True:
        dist=abs(chicken[j][0]-x)+abs(chicken[j][1]-y)
        cand=min(cand,dist)
    answer+=cand
  answers.append(answer)
      
    
  

# 백트래킹으로 치킨집 조합 m 개를 구한다.
def back(idx,cnt):
  if cnt==m:
    findMinVal()
    return
  for i in range(idx,len(chicken)): 
    visited[i]=True
    back(i+1,cnt+1)
    visited[i]=False
    
back(0,0) 

print(min(answers))
