n = int(input())
lst = list(map(int, input().split()))

# dp[i]는 lst[i]까지 고려했을 때 LIS의 최대 길이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 부분 수열의 길이 출력
print(max(dp))
