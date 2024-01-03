import sys

n=int(sys.stdin.readline())

ans=sorted(list(map(int,sys.stdin.readline().split())))

answer=0
tmp=0
for i in range(0,n):
  answer=answer+ans[i]
  tmp+=answer

print(tmp)