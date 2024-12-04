import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  # 문제를 나누는 기준 찾기 
  # 소문제를 나누는 기준은 n 값이다. 
  n=int(input())
  
  # 점화식 찾기
  # 각 0과 1에 대해, 피보나치 정의에 따라 dp[n]=dp[n-1]+dp[n-2] 값이 점화식이다.
  dp0=[0 for _ in range(n+1)]
  dp1=[0 for _ in range(n+1)]
  
  # 초기화 하기
  # 이때, 점화식에 따라 n이 1일 때와 0일 때는 음수가 아닌 정수 값을 가지는 dp 값이 없으므로 초기화 대상이다.
  if n==0:
    print(1,0)
    continue
  elif n==1:
    print(0,1)
    continue
  
  dp0[0], dp0[1] = 1,0
  dp1[0], dp1[1] = 0,1
  
  # 점화식을 사용하여 반복문으로 bottom-up 방식을 사용해 dp0[n] 값과 dp1[n] 값을 계산한다.
  for i in range(2,n+1):
    dp0[i]=dp0[i-1]+dp0[i-2]
    dp1[i]=dp1[i-1]+dp1[i-2]
  
  print(dp0[n], dp1[n])


