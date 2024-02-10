import sys

input=sys.stdin.readline

n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]

#백트래킹 조합
m=int(n/2)
members=[i for i in range(n)]

def bact_p(picked):
  ans=0
  for i in picked:
    for j in picked:
      if j!=i:
        ans+=board[i][j]
  return ans

ans=[]

#0부터 n-1 까지의 숫자 중에서 m개 선택하기

ans=[]
def bact_c(cnt,i):
  if cnt==m:
    link=list(set(members)-set(start))
    sn=bact_p(start)
    ln=bact_p(link)
    ans.append(abs(sn-ln))    
    return
  for t in range(i+1, n):
    start.append(t)
    bact_c(cnt+1,t)
    start.pop()

for i in range(n-m+1):
  start=[i]
  bact_c(1,i)

print(min(ans))
  