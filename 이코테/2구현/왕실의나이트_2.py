import sys

input=sys.stdin.readline

lst=list(map(str,input().rstrip()))

dir=[(2,-1),(2,1),(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2)]
answer=0
for x,y in dir:
  if 0<=ord(lst[0])-ord('a')+x<8 and 0<int(lst[1])+y<=8:
    answer+=1

print(answer)
