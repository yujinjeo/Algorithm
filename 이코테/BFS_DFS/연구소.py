import sys
from collections import deque
from copy import deepcopy

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
## 가장 어려웠던 벽 세우기... 
# 어찌됐든 브루트포스이지만, 처음에는 make_wall의 매개변수로 cand를 넣는 방식으로 진행했다.
# 
def make_wall(cnt):
  if cnt == 3:
    spread()
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
  global answer
  cand = deepcopy(board)
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
  # 처음에는 count 함수를 따로 만들어 이중반복문으로 0의 개수를 찾았다. list의 count 함수를 사용하면 훨씬 쉽고 빠르게 값의 개수를 찾을 수 있다.
  for i in range(n):
    safe += cand[i].count(0)
  answer = max(answer, safe)


# 3개 고르기
make_wall(0)
print(answer)


## walls set 안에 wall set을 넣으려고 했더니 넣어지지 않았다. set은 변화 가능한 객체이므로 walls set 안에 
# 넣을 수 없다. set 안에 set을 넣으려면 frozenset()처리를 한 후 넣을 수 있다.
