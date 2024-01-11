import sys

n,m=map(int, sys.stdin.readline().split())

#문자열을 배열로 받을 때는 strip() 처리를 한 다음에 list로 변환하면 쉽게 받을 수 있다.
floor=[list(sys.stdin.readline().strip()) for _ in range(n)]

#dfs는 조건에 맞으면->거기로 이동! 하는 방식으로 깊게, 더 깊게 들어가는 방식이기 때문에 
#여러 부분을 돌고 싶다면 반복문 안에 조건문 처리를 해서 dfs를 구현할 수 있다.
def dfs(i,j):
  if floor[i][j]=="-":
    #내가 실수했던 부분: 값을 확인하고 나서 'f'로 바꾸기!! 확인도 전에 바꿔서 계속 이상한 값이 나왔다ㅠㅠ
    floor[i][j]="f"
    for dj in [-1,1]:
      x=i
      y=dj+j
      if 0<=y<m:
        if floor[x][y]=="-":
          dfs(x,y)
  if floor[i][j]=="|":
    floor[i][j]="f"
    for di in [-1,1]:
      x=di+i
      y=j
      if 0<=x<n:
        if floor[x][y]=="|":
          dfs(x,y)
                 
cnt=0
for i in range(n):
  for j in range(m):
    if floor[i][j]!="f":
      dfs(i,j)
      cnt+=1
    else:
      continue

print(cnt)