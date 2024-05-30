import sys
from collections import deque
import copy

input = sys.stdin.readline
n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
virus = []
for i in range(n):
  for j in range(m):
    if board[i][j] == 2:
      virus.append((i, j))

answer = 0
# 벽 세우기
def make_wall(cnt):
  global answer
  if cnt == 3:
    safe = spread()
    answer = max(answer, safe)
    return
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        board[i][j] = 1
        make_wall(cnt + 1)
        board[i][j] = 0


d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


# 퍼뜨리기
def spread():
  cand = copy.deepcopy(board)
  q = deque(virus)
  while q:
    i, j = q.popleft()
    for k in range(4):
      dx, dy = d[k]
      x = i + dx
      y = j + dy
      if 0 <= x < n and 0 <= y < m and cand[x][y] == 0:
        cand[x][y] = 2
        q.append((x, y))
  safe=0
  for i in range(n):
    safe += cand[i].count(0)
  return safe


# 3개 고르기
make_wall(0)

print(answer)
