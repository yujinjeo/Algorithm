import sys

n=int(input())

trngl=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(1,n):
  for j in range(len(trngl[i])):
    if j-1<0:
      trngl[i][j]+=trngl[i-1][j]
    elif j>=len(trngl[i-1]):
      trngl[i][j]+=trngl[i-1][j-1]
    else:
      trngl[i][j]+=max(trngl[i-1][j-1], trngl[i-1][j])

print(max(trngl[n-1]))