import sys

input = sys.stdin.readline

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

if n==1:
    print(board[0][0])
    sys.exit()

def func(x,y,radius):
    if radius==1:
        return board[x][y]
    lu=func(x,y,radius//2)
    ru=func(x+radius//2,y,radius//2)
    ld=func(x,y+radius//2,radius//2)
    rd=func(x+radius//2,y+radius//2,radius//2)

    lst=[lu,ru, ld, rd]
    lst.sort()
    
    return lst[1]

a=func(0,0,n)
print(a) 
