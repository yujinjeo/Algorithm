import sys

input = sys.stdin.readline

n,m=map(int,input().split(' '))
A=[list(map(int,input().rstrip())) for _ in range(n)]
B=[list(map(int,input().rstrip())) for _ in range(n)]
ans=0

def flip(x,y):
  for i in range(x, x+3):
    for j in range(y, y+3):
        A[i][j]=(A[i][j]+1)%2

def is_same():
  for i in range(n):
    for j in range(m):
      if A[i][j]!=B[i][j]:
        return False
  return True


if (n<3 or m<3) and not is_same():
  ans=-1
else:
  for i in range(n-2):
    for j in range(m-2):
      if A[i][j]!=B[i][j]:
        flip(i,j)
        ans+=1
  if not is_same():
    ans=-1
  
print(ans)

