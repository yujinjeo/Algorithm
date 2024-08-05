import sys

input = sys.stdin.readline

n=int(input())
lst=[]
for i in range(n):
  a,b=map(str,input().split())
  b=int(b)
  lst.append((a,b))

# 오름차순이다
lst=sorted(lst,key=lambda x:x[1])

for a,b in lst:
  print(a,end=' ')


