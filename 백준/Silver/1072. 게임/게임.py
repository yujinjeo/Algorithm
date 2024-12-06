
# 이진 탐색
x,y=map(int,input().split(' '))
z=int(y*100/x)

# 승률이 변하는지 확인
def check(i):
  cand=int((y+i)*100/(x+i))
  return True if cand>z else False


# 변수는 추가 게임 횟수
# start와 end는 0과 x
start,end=1,x
ans=-1
while start<=end:
  mid=(start+end)//2
  if check(mid):
    ans=mid
    end=mid-1
  else:
    start=mid+1

print(ans)