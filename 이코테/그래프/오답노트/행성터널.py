import sys
import heapq

q=[]
input=sys.stdin.readline
n=int(input())
parent=[i for i in range(n)]

def find_parent(x):
  if x!=parent[x]:
    parent[x]=find_parent(parent[x])
  return parent[x]

def union(a,b):
  x=find_parent(a)
  y=find_parent(b)
  if x<y:
    parent[y]=x
  else:
    parent[x]=y



# sol2 
x=[]
y=[]
z=[]
for i in range(n):
  a,b,c=map(int,input().split())
  x.append((a,i))
  y.append((b,i))
  z.append((c,i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
  heapq.heappush(q,(x[i+1][0]-x[i][0],x[i+1][1],x[i][1]))
  heapq.heappush(q,(y[i+1][0]-y[i][0],y[i+1][1],y[i][1]))
  heapq.heappush(q,(z[i+1][0]-z[i][0],z[i+1][1],z[i][1]))

# planet=[]
# for i in range(n):
#   x,y,z=map(int,input().split())
#   planet.append((x,y,z))


# # 나의 풀이 : 이렇게 모든 길이를 다 찾는 것보다, x, y, z 별로 길이를 찾는 게 더 쉽다. 어차피 가장 짧은 길이를 찾는 것이므로, sort하여 짧은 길이끼리 heap에 넣는 게 좋다. 
# for i in range(n-1):
#   for j in range(i+1,n):
#     dis=min(abs(planet[i][0]-planet[j][0]),abs(planet[i][1]-planet[j][1]),abs(planet[i][2]-planet[j][2])) 
#     heapq.heappush(q,(dis,i,j))

answer=0
while q:
  dis,a,b=heapq.heappop(q)
  if find_parent(a)!=find_parent(b):
    union(a,b)
    answer+=dis

print(answer)


