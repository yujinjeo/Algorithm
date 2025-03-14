import sys
input = sys.stdin.readline

s, n, k, r1, r2, c1, c2 = map(int,input().split())

# 범위는 (r1, c1) ~ (r2, c2)
board=[['0']*(c2-c1+1) for _ in range(r2-r1+1)]

def func(x,y, r, t):
    global board
        
    radius = (r//n)*k
    start = (r - radius)//2

    sx=x+start
    ex=x+start+radius
    sy=y+start
    ey=y+start+radius
    
    for i in range(max(sx,r1), min(ex,r2+1)):
        for j in range(max(sy,c1), min(ey,c2+1)):
            board[i-r1][j-c1]='1'

    if t-1==0:
        return 
        
    new_r=n**(t-1)

    for i in range(n):
        for j in range(n):
            a=x+new_r*i
            b=y+new_r*j
            if sx<=a<ex and sy<=b<ey:
                continue
            if a>r2 or a+new_r<r1 or b>c2 or b+new_r<c1:
                continue
            func(a,b, new_r, t-1)

if s==0:
    print('0')
else:
    func(0,0,n**s,s)
    for i in range(len(board)):
        print(''.join(board[i]))
    