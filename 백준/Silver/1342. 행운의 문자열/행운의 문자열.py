lst=list(map(str,input().rstrip()))

n=len(lst)

answer=set()
def bact(word,l):
  if l==n:
      answer.add(word)
      return
  for i in range(n):
    if not visited[i] and word[l-1]!=lst[i]:
      visited[i]=True
      bact(word+lst[i],l+1)
      visited[i]=False

for i in range(n):
  visited=[False]*n
  visited[i]=True
  bact(str(lst[i]),1)

print(len(answer))
  

