import sys

ss=sys.stdin.readline().strip()
idx=0
line="1"
start=0
next=1
c=1

while True:
  if idx==len(ss):
    break
  s=start
  for i in range(s,next):
    if idx<len(ss) and ss[idx]==line[i]:
      idx+=1
      start+=1
      continue
    start+=1
  c+=1
  line+=str(c)
  next+=len(str(c))
  

print(c-1)