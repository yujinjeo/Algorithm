import sys

n=int(sys.stdin.readline())

files=[]
for _ in range(n):
  files.append(sys.stdin.readline())

lnth=len(files[0])
ans=""
word=files[0]
for i in range(lnth):
  thisword=word[i]
  flag=0
  for j in range(n):
    if files[j][i]!=thisword:
      flag=1
  if flag==0:
    ans+=thisword
  else:
    ans+="?"

print(ans)
