import sys

input = sys.stdin.readline

n,m=map(int,input().split())
x,y,d = map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]

# 삼성역량테스트 로봇청소기 풀기!
# 북, 동, 남, 서
dir=[(-1,0),(0,1),(1,0),(0,-1)]

# 반시계방향은 북 서 남 동동

answer=0

while True:
  if board[x][y]==0:
    # 청소된 부분은 벽이 아니다! 1과 2 구분
    board[x][y]+=2
    answer+=1
  flag=0
  # 탐색 시, 첫 방향이 현재 방향이 아니라 왼쪽으로 회전한 방향이 첫 방향이었다..!
  for i in range(3,-1,-1):
    dx,dy=dir[(d+i)%4]
    a=x+dx
    b=y+dy
    if 0<=a<n and 0<=b<m and board[a][b]==0:
      d=(d+i)%4
      x,y=a,b
      flag=1
      break
  if flag==0:
    dx,dy=dir[d]
    a=x-dx
    b=y-dy
    if 0<=a<n and 0<=b<m and board[a][b]!=1:
      x,y=a,b
    else:
      break
print(board)
print(answer)
  
