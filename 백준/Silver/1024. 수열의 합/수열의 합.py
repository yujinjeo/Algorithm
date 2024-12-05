import sys

input = sys.stdin.readline

# 등차수열의 합 공식
n,l = map(int,input().split(' '))
ans=[]
while True:
  if l>100:
    print(-1)
    break

  x=n-l*(l-1)/2
  if x<0:
    print(-1)
    break
  if x%l==0:
    x=int(x/l)
    ans=[i for i in range(x,x+l)]
    break
  else:
    l+=1

print(*ans)
    

