import sys
input=sys.stdin.readline

l=input().strip()
x=ord(l[0])-ord('a')+1
y=int(l[1])

dx=[2,2,-2,-2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2]
answer=0

for i in range(len(dx)):
  a=x+dx[i]
  b=y+dy[i]
  if 0<a<=8 and 0<b<=8:
    answer+=1

print(answer)
