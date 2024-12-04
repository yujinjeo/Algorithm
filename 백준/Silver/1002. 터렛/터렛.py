import sys, math

input = sys.stdin.readline

t=int(input())
ans=[]

for _ in range(t):
  x1,y1,r1,x2,y2,r2 = map(int,input().split(' '))

  r = math.sqrt((x1-x2)**2 + (y1-y2)**2)

  
  if (x1==x2) and (y1==y2):
    # 완전히 일치하는 경우
    if r1==r2:
      ans.append(-1)
    # 중심만 같고 반지름이 다른 경우
    else:
      ans.append(0)
  # 한 점에서 만나는 경우
  elif (r==r1+r2) or (r+min(r1,r2)==max(r1,r2)):
    ans.append(1)
  # 만나지 않는 경우
  elif (r>r1+r2) or (r+min(r1,r2)<max(r1,r2)):
    ans.append(0)
  # 두 점에서 만나는 경
  else:
    ans.append(2)

for a in ans:
  print(a)
      

