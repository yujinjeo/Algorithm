# sol 1

n, target=map(int,input().split())

lst=[int(input().rstrip()) for _ in range(n)]

dp=[0 for _ in range(target+1)]

lst.sort()

for i in range(target+1):
  val=10001
  for c in lst:
    if i-c==0:
      val=1
      break
    if i-c>=lst[0]:
      val=min(dp[i-c]+1, val)
  if val==10001:
    dp[i]=0
  else:
    dp[i]=val

if dp[target]==0:
  print(-1)
else:
  print(dp[target])


# sol 2 이코테 

n, target=map(int,input().split())

lst=[int(input().rstrip()) for _ in range(n)]

dp=[10001 for _ in range(10001)]
dp[0]=0
lst.sort()

for i in range(n):
  for j in range(lst[i], target+1):
    if dp[j-lst[i]]!=10001:
      dp[j]=min(dp[j],dp[j-lst[i]]+1)

if dp[target]==10001:
  print(-1)
else:
  print(dp[target])

