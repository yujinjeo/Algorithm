import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ssize = 2
r, c = 0, 0

# 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            r, c = i, j
            board[r][c] = 0

# 상하좌우 이동 방향
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 물고기를 찾으면서 최단 거리를 구하는 BFS
def find_prey(x, y):
    global ssize
    visited = [[False] * n for _ in range(n)]
    q = deque([(x, y, 0)])  # (x좌표, y좌표, 거리)
    visited[x][y] = True
    preys = []
    min_dist = 1e9

    while q:
        a, b, dist = q.popleft()

        # 최소 거리보다 멀리 떨어진 곳은 더 이상 탐색하지 않음
        if dist > min_dist:
            continue

        # 먹을 수 있는 물고기를 찾음
        if 0 < board[a][b] < ssize:
            preys.append((dist, a, b))
            min_dist = dist  # 먹을 수 있는 물고기의 거리 갱신
            continue

        for dx, dy in d:
            nx, ny = a + dx, b + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] <= ssize:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    # 먹을 수 있는 물고기 중 가장 위, 왼쪽에 있는 물고기 선택
    if preys:
        preys.sort(key=lambda x: (x[0], x[1], x[2]))  # 거리, 행, 열 순으로 정렬
        return preys[0]  # (거리, x좌표, y좌표)
    else:
        return None

answer = 0
fish = 0

while True:
    result = find_prey(r, c)
    if result is None:
        break

    # 물고기까지 이동하여 먹음
    dist, new_r, new_c = result
    answer += dist
    r, c = new_r, new_c
    board[r][c] = 0
    fish += 1

    # 상어 크기 증가 체크
    if fish == ssize:
        ssize += 1
        fish = 0

print(answer)