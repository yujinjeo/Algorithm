import sys

input = sys.stdin.readline

n,c,w=map(int,input().split(' '))
lst=[int(input()) for _ in range(n)]

def cal(x):
  total=0
  for v in lst:
    i=0
    j=0
    if v<x:
      continue
    if v%x==0:
      j+=v//x-1
    else:
      j+=v//x
    i=v//x
    profit = i*w*x - j*c
    if profit>0:
      total += profit
  return total  


maxv=0

for i in range(1,max(lst)+1):
  maxv=max(maxv, cal(i))

print(maxv)
  
  

