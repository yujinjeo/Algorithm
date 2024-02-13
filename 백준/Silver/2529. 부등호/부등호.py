import sys

input=sys.stdin.readline

n=int(input())
lst=list(map(str,input().strip().split()))
numbers=[i for i in range(10)]

ans=[]
#백트래킹 순열
def bact(cnt):
  if cnt==n+1:
    ans.append(list(picked))
    return
  for i in range(10):
    if visited[i]==False:
      if lst[cnt-1]=='<' and picked[cnt-1]<numbers[i]:
        visited[i]=True
        picked.append(numbers[i])
        bact(cnt+1)
        visited[i]=False
        picked.pop()
      elif lst[cnt-1]=='>' and picked[cnt-1]>numbers[i]:
        visited[i]=True
        picked.append(numbers[i])
        bact(cnt+1)
        visited[i]=False
        picked.pop()

for i in range(10):
  picked=[numbers[i]]
  visited=[False]*(10)
  visited[i]=True
  bact(1)

ans=sorted(ans)

minlst=''.join(map(str,ans[0]))
maxlst=''.join(map(str,ans[-1]))

print(maxlst)
print(minlst)

