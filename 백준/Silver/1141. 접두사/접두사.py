import sys

n=int(sys.stdin.readline())
lst=[]

for i in range(n):
  lst.append(sys.stdin.readline().strip())

lst=sorted(lst,key=lambda x:(x,len(x)))
cnt=1

for i in range(1,n):
  if lst[i-1] not in lst[i][0:len(lst[i-1])]:
    cnt+=1
    
print(cnt)