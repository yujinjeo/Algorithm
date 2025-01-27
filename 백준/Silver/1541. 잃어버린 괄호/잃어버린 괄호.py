import sys

input = sys.stdin.readline

s=input().rstrip().split('-')
ans=0

cand=s[0].split('+')
ans=sum(map(int,s[0].split('+')))

for element in s[1:]:
    ans-=sum(map(int,element.split('+')))

print(ans)


