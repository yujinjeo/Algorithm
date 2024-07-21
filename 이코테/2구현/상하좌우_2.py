import sys

input= sys.stdin.readline

n=int(input())
lst=list(map(str,input().rstrip().split(' ')))

dic={'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
x,y=0,0
for c in lst:
  a,b=dic[c]
  if 0<=x+a<n and 0<=y+b<n:
    x+=a
    y+=b

print(x+1,y+1)
