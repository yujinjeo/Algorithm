import sys
input = sys.stdin.readline

INF = 10**9

n, m = map(int, input().split())
board = [[INF for _ in range(n+1)] for _ in range(n+1)]

# 자기 자신으로의 거리는 0
for i in range(1, n+1):
    board[i][i] = 0

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1
    board[b][a] = 1

# 플로이드-워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

# 최소 케빈 베이컨 수 찾기
minv = INF
answer = 0

for i in range(1, n+1):
    val = sum(board[i][j] for j in range(1, n+1) if board[i][j] != INF)
    if val < minv:
        minv = val
        answer = i

print(answer)
