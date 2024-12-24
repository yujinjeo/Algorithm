import sys
input = sys.stdin.readline

# 입력 처리
n, s, m = map(int, input().split())
lst = list(map(int, input().split()))

# DP 배열 초기화
dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True  # 시작 볼륨 설정

# DP 수행
for i in range(n):
    for v in range(m + 1):
        if dp[i][v]:
            if v + lst[i] <= m:
                dp[i + 1][v + lst[i]] = True
            if v - lst[i] >= 0:
                dp[i + 1][v - lst[i]] = True

# 마지막 곡에서 가능한 최댓값 찾기
result = -1
for v in range(m, -1, -1):
    if dp[n][v]:
        result = v
        break

print(result)
