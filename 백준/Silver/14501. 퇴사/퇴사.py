import sys

input=sys.stdin.readline

n=int(input())
time=[]
period=[]
for i in range(n):
  t,p=map(int,input().split(' '))
  time.append(t)
  period.append(p)

dp=[0 for _ in range(n+1)]

# # 아마 이건, 기간과 시간이라는 변수가 2개가 있기 때문에, 전통적인 bottom up 방식과 약간 다른 점이 있을 거다.
# dp의 각 인덱스 별 들어가는 값의 의미는, i까지 고려했을 때 최대값이다. n을 반드시 마지막으로 포항했을 때 찾을 수 있는 값이 아니다.

# 아니, 정확히 왜 이렇게 할수밖에 없는가? 
# 이건 앞에 기간이 있는 경우이기 때문이다. 지금 내가 이걸 했을 때 다음 일의 유무가
# 내가 이 선택을 했을 때 dp가 업데이트 되는 범위가, dp 전체이기 때문에, 기록을 해놓을 수밖에 없다. 

for i in range(n):
  if i+time[i]<=n:
    dp[i+time[i]:]=list(map(lambda x: max(x,dp[i]+period[i]) ,dp[i+time[i]:]))

print(dp[-1])

  