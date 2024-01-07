import sys

n=int(sys.stdin.readline())

lst=[]

for _ in range(n):
  x,y=map(int, sys.stdin.readline().split())
  lst.append(y-x)

lst.sort()

if n%2==1:
  print(1)
else:
  print(lst[n//2]-lst[n//2-1]+1)