import sys

input = sys.stdin.readline

n=int(input())
lst=[int(input()) for _ in range(n)]

lst.sort(reverse=True)
ans=0
for i in range(n):
    if lst[i]-i>0:
        ans+=lst[i]-i

print(ans)