import sys

input = sys.stdin.readline

board = []
for i in range(19):
    board.append(list(map(int, input().split())))

directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

def valid_pos(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def check_omok(x, y, color):
    for dx, dy in directions:
        cnt = 1  # 현재 돌 포함
        nx, ny = x + dx, y + dy
        
        # 한 방향으로 체크
        while valid_pos(nx, ny) and board[nx][ny] == color:
            cnt += 1
            nx += dx
            ny += dy
        
        # 반대 방향 체크
        nx, ny = x - dx, y - dy
        while valid_pos(nx, ny) and board[nx][ny] == color:
            cnt += 1
            nx -= dx
            ny -= dy
        
        # 정확히 5개 연속인지 확인
        if cnt == 5:
            # 시작점이 가장 작은지 확인
            prev_x, prev_y = x - dx, y - dy
            if not valid_pos(prev_x, prev_y) or board[prev_x][prev_y] != color:
                return True
    return False

for i in range(19):
    for j in range(19):
        if board[i][j] == 1 or board[i][j] == 2:
            if check_omok(i, j, board[i][j]):
                print(board[i][j])
                print(i + 1, j + 1)
                sys.exit(0)

print(0)
