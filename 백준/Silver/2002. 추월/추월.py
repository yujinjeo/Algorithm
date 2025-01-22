import sys

input = sys.stdin.readline

n=int(input())

dic={}
for i in range(n):
    s=input().rstrip()
    dic[s]=i

ans=0

lst=[input().rstrip() for _ in range(n)]

for i in range(n):
    c=dic[lst[i]]
    for j in range(i+1,n):
        if dic[lst[j]]<c:
            ans+=1
            break 
print(ans)

