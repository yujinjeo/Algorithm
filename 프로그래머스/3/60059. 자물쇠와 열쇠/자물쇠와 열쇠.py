def turn_left(key, m):
    return [[key[j][m - 1 - i] for j in range(m)] for i in range(m)]

def copy_lock(lock, n):
    lock_extended = [[1 for _ in range(3 * n)] for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            lock_extended[i + n][j + n] = lock[i][j]
    return lock_extended

def is_open(key, lock, n, m):
    lock_extended = copy_lock(lock, n)
    for x in range(2 * n):
        for y in range(2 * n):
            for i in range(m):
                for j in range(m):
                    lock_extended[x + i][y + j] += key[i][j]
            if check(lock_extended, n):
                return True
            lock_extended = copy_lock(lock, n)
    return False

def check(lock, n):
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    for _ in range(4):
        if is_open(key, lock, n, m):
            return True
        key = turn_left(key, m)
    return False

# def turn_left(key,m):
#     ckey=[[0 for i in range(m)] for _ in range(m)]
#     for i in range(m):
#         for j in range(m):
#             x=j
#             y=m-1-i
#             ckey[x][y]=key[i][j]
#     return ckey

# def copyl(clock,n):
#     lock_=[[1 for _ in range(3*n)] for _ in range(3*n)]
#     for i in range(n):
#         for j in range(n):
#             lock_[i+n][j+n]=clock[i][j]
#     return lock_

# def isopen(ckey, clock, n,m):
#     llock=copyl(clock,n)
#     for x in range(3*n-1-m-1):
#         for y in range(3*n-1-m-1):
#             for i in range(0,m):
#                 for j in range(0,m):
#                     clock[x+i][y+j]+=ckey[i][j]
#             if 0 not in clock and 2 not in clock:
#                 return True
#             clock=copyl(llock,n)
                       
#     return False          

# def solution(key, lock):
#     answer = True
#     m=len(key)
#     n=len(lock)
    
#     lock_=[[1 for _ in range(3*n)] for _ in range(3*n)]
#     for i in range(n):
#         for j in range(n):
#             lock_[i+n][j+n]=lock[i][j]
#     ckey=key
#     for i in range(4):
#         ckey=turn_left(ckey,m)
#         clock=lock_
        
#         if (isopen(ckey,clock,n,m)):
#             answer=True
#         else:
#             answer=False
#     return answer

