r,c,k=map(int,input().split(' '))
board=[list(map(str,input().rstrip())) for _ in range(r)]

d=[(0,1),(0,-1),(1,0),(-1,0)]
visited=[[False for _ in range(c)] for _ in range(r)]
visited[r-1][0]=True
dist=[]
def dfs(x,y,depth):
  if x==0 and y==c-1:
    dist.append(depth)
    return
  for i in range(4):
    a=x+d[i][0]
    b=y+d[i][1]
    if 0<=a<r and 0<=b<c and not visited[a][b] and board[a][b]=='.':
      visited[a][b]=True
      dfs(a,b,depth+1)
      visited[a][b]=False
dfs(r-1,0,1)
print(dist.count(k))
  

