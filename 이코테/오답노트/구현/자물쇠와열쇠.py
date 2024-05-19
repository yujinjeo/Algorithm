
def turn_left(key,m):
    ckey=[[0 for i in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            x=j
            y=m-1-i
            ckey[x][y]=key[i][j]
    return ckey

def copyl(clock,n):
    lock_=[[1 for _ in range(3*n)] for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            lock_[i+n][j+n]=clock[i][j]
    return lock_

def compare(clock,n):
    for i in range(n,2*n):
        for j in range(n,2*n):
            if clock[i][j]!=1:
                return False
    return True

def isopen(ckey, clock, n,m):
    llock=copyl(clock,n)
    for x in range(2*n):
        for y in range(2*n):
            for i in range(0,m):
                for j in range(0,m):
                    llock[x+i][y+j]+=ckey[i][j]
            if compare(llock,n):
                return True
            llock=copyl(clock,n)
                       
    return False          

def solution(key, lock):
    answer = True
    m=len(key)
    n=len(lock)
    
    for i in range(4):
        if isopen(key,lock,n,m):
            return True
        
        key=turn_left(key,m)
    return False

