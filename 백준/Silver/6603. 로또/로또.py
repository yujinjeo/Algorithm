import sys

input=sys.stdin.readline

def bact(picked, cnt ,idx):
  if cnt==0:
    print(*picked)
    #ans.append(picked)
    return
  if k-cnt<idx:
    return
  for i in range(idx+1,k-cnt+1):
    picked.append(lst[i])
    bact(picked, cnt-1, i)
    picked.pop()

while True:
  line=input().strip()
  if line=='0':
    break
  lst=list(map(int,line.split()))
  k=lst.pop(0)

  ans=[]
  for i in range(k-6+1):
    picked=[lst[i]]
    bact(picked,5,i)

  print()
