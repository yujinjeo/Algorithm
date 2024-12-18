import sys

input = sys.stdin.readline

n,m=map(int,input().split(' '))
board=[list(map(str,input().rstrip())) for _ in range(n)]

count=0

def flip(x,y):
  for i in range(x):
    for j in range(y):
      if board[i][j]=='1':
        board[i][j]='0'
      else:
        board[i][j]='1'

for i in range(n-1,-1,-1):
  for j in range(m-1,-1,-1):
    if board[i][j]=='1':
      flip(i+1,j+1)
      count+=1

print(count)
    
      

