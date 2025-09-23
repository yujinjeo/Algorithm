from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 초기 위치
rx = ry = bx = by = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'

d = [(-1,0),(1,0),(0,-1),(0,1)]  # 상하좌우

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = True
    
    while q:
        rxx, ryy, bxx, byy, cnt = q.popleft()
        if cnt >= 10:
            break
        for dx, dy in d:
            nrx, nry, rc = move(rxx, ryy, dx, dy)
            nbx, nby, bc = move(bxx, byy, dx, dy)
            
            if board[nbx][nby] == 'O':  # 파란 구슬 들어감
                continue
            if board[nrx][nry] == 'O':  # 빨간 구슬만 들어감
                return cnt+1
            
            # 겹친 경우 -> 더 많이 움직인 애를 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, cnt+1))
    return -1

print(bfs())
