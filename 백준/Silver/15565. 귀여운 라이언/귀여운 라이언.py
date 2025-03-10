import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

il1 = deque()
cnt1 = 0

# 처음 k개의 '1'을 포함하는 부분 찾기
for i in range(n):
    if lst[i] == 1:
        il1.append(i)
        cnt1 += 1
        if cnt1 == k:
            break

# k개의 '1'을 포함하지 못하면 -1 출력 후 종료
if len(il1) < k:
    print(-1)
    sys.exit()
elif k == 1:
    print(1)
    sys.exit()

# 최소 구간 길이 저장
current1 = il1[-1] - il1[0] + 1
min_length = current1

# 슬라이딩 윈도우 탐색
for i in range(il1[-1] + 1, n):
    if lst[i] == 1:
        il1.append(i)  # 새로운 '1' 추가
        il1.popleft()  # 첫 번째 '1' 제거

        # 새로운 최소 구간 길이 갱신
        current1 = il1[-1] - il1[0] + 1
        min_length = min(min_length, current1)

print(min_length)
