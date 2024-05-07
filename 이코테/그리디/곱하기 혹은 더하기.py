import sys
input=sys.stdin.readline

tmp=input().strip()
n=len(tmp)
lst=[]
for i in range(n):
  lst.append(int(tmp[i]))

lst.sort(reverse=True)
no=[0,1]

answer=0
for i in range(n):
  if answer in no or lst[i] in no:
    answer+=lst[i]
  else:
    answer*=lst[i]

print(answer)
